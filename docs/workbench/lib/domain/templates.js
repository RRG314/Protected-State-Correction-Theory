export const LINEAR_TEMPLATE_LIBRARY = {
  sensor_basis: {
    label: '3-state static record template',
    candidates: [
      { id: 'measure_x1', label: 'measure x1', row: [1, 0, 0] },
      { id: 'measure_x2', label: 'measure x2', row: [0, 1, 0] },
      { id: 'measure_x3', label: 'measure x3', row: [0, 0, 1] },
      { id: 'measure_x2_plus_x3', label: 'measure x2+x3', row: [0, 1, 1] },
      { id: 'measure_x1_plus_x2', label: 'measure x1+x2', row: [1, 1, 0] },
    ],
    protectedOptions: {
      x3: { label: 'coordinate x3', rows: [[0, 0, 1]] },
      x2_plus_x3: { label: 'sum x2+x3', rows: [[0, 1, 1]] },
      tail_pair: { label: 'tail pair (x2, x3)', rows: [[0, 1, 0], [0, 0, 1]] },
      full_state: {
        label: 'full state (x1, x2, x3)',
        rows: [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
      },
    },
    defaultMeasurements: ['measure_x1', 'measure_x2_plus_x3'],
  },
};

