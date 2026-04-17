(function () {
  const steps = Array.from(document.querySelectorAll('.learning-step'));
  const progressLabel = document.getElementById('progress-label');
  const progressBar = document.getElementById('progress-bar');
  const prevButton = document.getElementById('prev-step');
  const nextButton = document.getElementById('next-step');
  const healthNode = document.getElementById('asset-health');

  let activeStep = 0;

  function updateProgressUI() {
    if (!steps.length) return;
    const current = steps[activeStep];
    const stepIndex = Number(current.getAttribute('data-step-index') || activeStep + 1);
    const stepTitle = current.getAttribute('data-step-title') || `Step ${stepIndex}`;
    if (progressLabel) {
      progressLabel.textContent = `Step ${stepIndex} of ${steps.length}: ${stepTitle}`;
    }
    if (progressBar) {
      const ratio = stepIndex / steps.length;
      progressBar.style.width = `${Math.max(0, Math.min(100, ratio * 100))}%`;
    }
    if (prevButton) prevButton.disabled = activeStep <= 0;
    if (nextButton) nextButton.disabled = activeStep >= steps.length - 1;
  }

  function scrollToStep(index) {
    if (index < 0 || index >= steps.length) return;
    steps[index].scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  if (prevButton) {
    prevButton.addEventListener('click', () => scrollToStep(activeStep - 1));
  }
  if (nextButton) {
    nextButton.addEventListener('click', () => scrollToStep(activeStep + 1));
  }

  if ('IntersectionObserver' in window && steps.length) {
    const observer = new IntersectionObserver(
      (entries) => {
        let best = null;
        for (const entry of entries) {
          if (!entry.isIntersecting) continue;
          if (!best || entry.intersectionRatio > best.intersectionRatio) {
            best = entry;
          }
        }
        if (!best) return;
        const idx = steps.indexOf(best.target);
        if (idx >= 0 && idx !== activeStep) {
          activeStep = idx;
          updateProgressUI();
        }
      },
      { threshold: [0.15, 0.4, 0.7] }
    );
    steps.forEach((step) => observer.observe(step));
  }

  // Expandable image lightbox.
  const modal = document.getElementById('lightbox');
  const modalImg = document.getElementById('lightbox-image');
  const close = document.getElementById('lightbox-close');

  document.querySelectorAll('a[data-full-image]').forEach((link) => {
    link.addEventListener('click', (event) => {
      event.preventDefault();
      const src = link.getAttribute('data-full-image');
      if (!src || !modal || !modalImg) return;
      modalImg.src = src;
      modal.classList.add('open');
    });
  });

  function closeModal() {
    if (!modal || !modalImg) return;
    modal.classList.remove('open');
    modalImg.src = '';
  }

  if (close) close.addEventListener('click', closeModal);
  if (modal) {
    modal.addEventListener('click', (event) => {
      if (event.target === modal) closeModal();
    });
  }
  window.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeModal();
  });

  // Runtime visual health checks: images only.
  const imageNodes = Array.from(document.querySelectorAll('.visual-card img'));
  const totalAssets = imageNodes.length;
  let loadedAssets = 0;
  let failedAssets = 0;

  function updateHealth() {
    if (!healthNode) return;
    healthNode.textContent = `Visuals loaded: ${loadedAssets}/${totalAssets}${failedAssets > 0 ? ` (${failedAssets} failed)` : ''}`;
    healthNode.style.color = failedAssets > 0 ? '#9f1d35' : '#1d6f5f';
  }

  function markAssetSeen(node, ok, src) {
    if (node.dataset.healthDone === '1') return;
    node.dataset.healthDone = '1';
    loadedAssets += 1;
    if (!ok) {
      failedAssets += 1;
      const filename = (src || '').split('/').pop() || 'unknown-file';
      console.error(`[visual-health] missing visual asset: ${filename} (${src || 'no-src'})`);
      const fallback = document.createElement('div');
      fallback.className = 'missing-visual';
      fallback.textContent = `Missing visual: ${filename}`;
      node.replaceWith(fallback);
    }
    updateHealth();
  }

  imageNodes.forEach((node) => {
    const src = node.getAttribute('src') || '';
    if (!src) {
      markAssetSeen(node, false, src);
      return;
    }
    if (node.complete) {
      markAssetSeen(node, node.naturalWidth > 0, src);
    } else {
      node.addEventListener('load', () => markAssetSeen(node, true, src), { once: true });
      node.addEventListener('error', () => markAssetSeen(node, false, src), { once: true });
    }
  });

  // Video warnings only (codec support varies by browser).
  document.querySelectorAll('.visual-card video').forEach((video) => {
    const src = video.getAttribute('src') || 'unknown-video';
    video.addEventListener('error', () => {
      console.warn(`[visual-health] video failed to load in this browser: ${src}`);
    });
  });

  updateHealth();
  updateProgressUI();
})();
