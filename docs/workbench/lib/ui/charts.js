import { clamp } from '../compute.js';

export function vectorPlotSvg(analysis) {
  const size = 360;
  const half = size / 2;
  const scale = 90;
  const toPoint = (vector) => [half + vector[0] * scale, half - vector[1] * scale];
  const makeArrow = (vector, color, width) => {
    const [x2, y2] = toPoint(vector);
    return `<line x1="${half}" y1="${half}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="${width}" stroke-linecap="round" marker-end="url(#arrow-${color.replace('#', '')})" />`;
  };
  return `
    <svg viewBox="0 0 ${size} ${size}" aria-label="Exact projection plot">
      <defs>
        ${['#1f4b99', '#9c5b2a', '#1c1d21', '#a63229']
          .map(
            (color) => `
          <marker id="arrow-${color.replace('#', '')}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="${color}" />
          </marker>
        `
          )
          .join('')}
      </defs>
      <rect width="${size}" height="${size}" rx="18" fill="rgba(255,255,255,0.78)" />
      <line x1="0" y1="${half}" x2="${size}" y2="${half}" stroke="rgba(28,29,33,0.15)" />
      <line x1="${half}" y1="0" x2="${half}" y2="${size}" stroke="rgba(28,29,33,0.15)" />
      ${makeArrow(analysis.s, '#1f4b99', 4)}
      ${makeArrow(analysis.d, '#9c5b2a', 4)}
      ${makeArrow(analysis.x, '#1c1d21', 4)}
      ${makeArrow(analysis.recovered, '#a63229', 3)}
      <text x="16" y="28" fill="#5d625e" font-size="13">Overlap = ${analysis.overlap.toFixed(3)}</text>
      <text x="16" y="46" fill="#5d625e" font-size="13">Recovery error = ${analysis.exactError.toExponential(2)}</text>
    </svg>
  `;
}

export function barChartSvg(series) {
  const width = 540;
  const height = 260;
  const innerH = 180;
  const maxAbs = Math.max(...series.flatMap((entry) => entry.values.map((value) => Math.abs(value)))) || 1;
  const barWidth = 14;
  const gap = 8;
  const groupGap = 24;
  const colors = ['#1f4b99', '#9c5b2a', '#356c4a'];
  let x = 36;
  const bars = [];
  const labels = [];
  series.forEach((entry, groupIndex) => {
    entry.values.forEach((value, index) => {
      const scaled = (Math.abs(value) / maxAbs) * innerH;
      const y = value >= 0 ? 200 - scaled : 200;
      bars.push(`<rect x="${x}" y="${y}" width="${barWidth}" height="${scaled}" fill="${colors[groupIndex % colors.length]}" rx="4" />`);
      labels.push(`<text x="${x + barWidth / 2}" y="222" text-anchor="middle" font-size="11" fill="#5d625e">${index}</text>`);
      x += barWidth + gap;
    });
    labels.push(`<text x="${x - (entry.values.length * (barWidth + gap)) / 2 - 4}" y="244" text-anchor="middle" font-size="12" fill="#1c1d21">${entry.label}</text>`);
    x += groupGap;
  });
  return `
    <svg viewBox="0 0 ${width} ${height}" aria-label="QEC amplitude comparison">
      <rect width="${width}" height="${height}" rx="18" fill="rgba(255,255,255,0.78)" />
      <line x1="20" y1="200" x2="${width - 16}" y2="200" stroke="rgba(28,29,33,0.2)" />
      ${bars.join('')}
      ${labels.join('')}
    </svg>
  `;
}

export function lineChartSvg(points, xLabel, yLabel, markerX = null) {
  const finitePoints = points
    .map((point) => ({ x: Number(point.x), y: Number(point.y) }))
    .filter((point) => Number.isFinite(point.x) && Number.isFinite(point.y));
  const width = 540;
  const height = 260;
  const left = 48;
  const right = 18;
  const top = 18;
  const bottom = 42;
  if (!finitePoints.length) {
    return `
      <svg viewBox="0 0 ${width} ${height}" aria-label="Line chart unavailable">
        <rect width="${width}" height="${height}" rx="18" fill="rgba(255,255,255,0.78)" />
        <text x="${width / 2}" y="${height / 2 - 6}" text-anchor="middle" font-size="14" fill="#5d625e">No finite chart data</text>
        <text x="${width / 2}" y="${height / 2 + 18}" text-anchor="middle" font-size="12" fill="#8a8f8b">${xLabel} / ${yLabel}</text>
      </svg>
    `;
  }
  const xs = finitePoints.map((point) => point.x);
  const ys = finitePoints.map((point) => point.y);
  const xMin = Math.min(...xs);
  const xMax = Math.max(...xs);
  const yMin = Math.min(...ys);
  const yMax = Math.max(...ys);
  const xScale = (value) => left + ((value - xMin) / Math.max(xMax - xMin, 1e-9)) * (width - left - right);
  const yScale = (value) => height - bottom - ((value - yMin) / Math.max(yMax - yMin, 1e-9)) * (height - top - bottom);
  const path = finitePoints.map((point, index) => `${index === 0 ? 'M' : 'L'} ${xScale(point.x)} ${yScale(point.y)}`).join(' ');
  const marker = markerX === null
    ? ''
    : (() => {
        const numericMarker = Number(markerX);
        if (!Number.isFinite(numericMarker)) {
          return '';
        }
        const chosen = finitePoints.reduce((best, point) =>
          Math.abs(point.x - numericMarker) < Math.abs(best.x - numericMarker) ? point : best
        );
        const x = xScale(chosen.x);
        const y = yScale(chosen.y);
        return `
          <line x1="${x}" y1="${top}" x2="${x}" y2="${height - bottom}" stroke="rgba(28,29,33,0.18)" stroke-dasharray="5 5" />
          <circle cx="${x}" cy="${y}" r="5" fill="#1c1d21" stroke="#fffdf8" stroke-width="2" />
        `;
      })();
  return `
    <svg viewBox="0 0 ${width} ${height}" aria-label="Line chart">
      <rect width="${width}" height="${height}" rx="18" fill="rgba(255,255,255,0.78)" />
      <line x1="${left}" y1="${height - bottom}" x2="${width - right}" y2="${height - bottom}" stroke="rgba(28,29,33,0.18)" />
      <line x1="${left}" y1="${top}" x2="${left}" y2="${height - bottom}" stroke="rgba(28,29,33,0.18)" />
      <path d="${path}" fill="none" stroke="#9c5b2a" stroke-width="3" stroke-linecap="round" />
      ${marker}
      <text x="${width / 2}" y="${height - 10}" text-anchor="middle" font-size="12" fill="#5d625e">${xLabel}</text>
      <text x="16" y="${height / 2}" transform="rotate(-90 16 ${height / 2})" text-anchor="middle" font-size="12" fill="#5d625e">${yLabel}</text>
    </svg>
  `;
}

export function drawHeatmap(canvas, field) {
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const rows = field.length;
  const cols = field[0].length;
  const flat = field.flat();
  const maxAbs = Math.max(...flat.map((value) => Math.abs(value))) || 1;
  const cellW = canvas.width / cols;
  const cellH = canvas.height / rows;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (let i = 0; i < rows; i += 1) {
    for (let j = 0; j < cols; j += 1) {
      const value = clamp(field[i][j] / maxAbs, -1, 1);
      const red = value > 0 ? 190 + Math.round(55 * value) : 34 + Math.round(90 * (1 + value));
      const blue = value < 0 ? 190 + Math.round(55 * -value) : 45 + Math.round(70 * (1 - value));
      const green = 120 + Math.round(40 * (1 - Math.abs(value)));
      ctx.fillStyle = `rgb(${red}, ${green}, ${blue})`;
      ctx.fillRect(j * cellW, i * cellH, cellW + 0.5, cellH + 0.5);
    }
  }
}

export function matrixTable(matrix, labels) {
  return `
    <table class="matrix-table">
      <thead>
        <tr><th></th>${labels.map((label) => `<th>${label}</th>`).join('')}</tr>
      </thead>
      <tbody>
        ${matrix
          .map(
            (row, i) =>
              `<tr><th>${labels[i]}</th>${row.map((value) => `<td>${value.toFixed(3)}</td>`).join('')}</tr>`
          )
          .join('')}
      </tbody>
    </table>
  `;
}
