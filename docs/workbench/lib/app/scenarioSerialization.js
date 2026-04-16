import { DEFAULT_STATE } from '../domain/defaultState.js';

export function cloneState(value) {
  return JSON.parse(JSON.stringify(value));
}

export function sanitizeState(candidate) {
  const safe = cloneState(DEFAULT_STATE);
  if (!candidate || typeof candidate !== 'object') return safe;
  if (candidate.mode === 'technical') safe.mode = 'technical';
  if (typeof candidate.activeLab === 'string' && safe.labs[candidate.activeLab]) {
    safe.activeLab = candidate.activeLab;
  }
  for (const [lab, defaults] of Object.entries(safe.labs)) {
    if (candidate.labs?.[lab] && typeof candidate.labs[lab] === 'object') {
      for (const key of Object.keys(defaults)) {
        if (candidate.labs[lab][key] !== undefined) {
          safe.labs[lab][key] = candidate.labs[lab][key];
        }
      }
    }
  }
  return safe;
}

const encodeBase64 = (text) => {
  if (typeof btoa === 'function') {
    return btoa(unescape(encodeURIComponent(text)));
  }
  return Buffer.from(text, 'utf8').toString('base64');
};

const decodeBase64 = (text) => {
  if (typeof atob === 'function') {
    return decodeURIComponent(escape(atob(text)));
  }
  return Buffer.from(text, 'base64').toString('utf8');
};

export function encodeShareState(state) {
  const payload = JSON.stringify(sanitizeState(state));
  return encodeBase64(payload);
}

export function decodeShareState(hash) {
  try {
    const cleaned = hash.replace(/^#?state=/, '').trim();
    if (!cleaned) return null;
    const json = decodeBase64(cleaned);
    return sanitizeState(JSON.parse(json));
  } catch {
    return null;
  }
}
