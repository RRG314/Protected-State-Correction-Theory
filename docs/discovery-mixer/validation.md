# Discovery Mixer Validation

## Validation Surfaces

The Discovery Mixer is validated at several levels.

### Python math and report tests

- custom linear repair detection
- nonlinear custom-input rejection
- periodic hidden-support detection
- control history-threshold detection
- bounded-domain architecture replacement
- random-seed reproducibility
- demo bundle completeness

### Generated artifact consistency

- generated summary matches the current Python source reports

### Workbench static tests

- structured linear fix remains inside structured mode
- structured control fix remains inside structured mode
- unsupported nonlinear input is rejected clearly
- random mode is reproducible
- report and CSV exports include the expected mixer data

### Workbench example consistency

- generated workbench examples match current analysis outputs

### Browser smoke

- mixer route loads
- structured cases render
- diagnostics and recommendations display
- before/after panels render after valid recommendation application

## Credibility Rule

The browser pass is required because static tests alone cannot catch all UI failures.
The current mixer was kept only after a real browser pass caught and fixed a render-time formatting bug.
