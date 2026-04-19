# BH/Cosmology Keep-Demote-Cut Map

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

This map assigns each BH/cosmology block to a concrete destination.

## Keep (OCP narrow physics extension, explicitly branch-limited)

| Section/theme | Keep level | Labeling rule | Destination |
|---|---|---|---|
| Linearized gauge projection mapping to OCP language | Keep as interpretive bridge | `KNOWN / REFRAMED` | OCP `docs/physics/` note |
| GW Fisher degeneracy witness (`Mc` vs `eta`) | Keep as benchmark | `VALIDATED / NUMERICAL ONLY` + literature overlap note | OCP noncanonical physics benchmark |
| Cosmology probe alignment table (`H0`, `Omega_m`) | Keep as design-diagnostic example | identity marked trivial | OCP noncanonical physics benchmark |
| Hubble fiber-contamination toy diagnostic | Keep with strict caveats | model-dependent, exploratory only | OCP noncanonical physics benchmark |
| Corrected BH thermodynamic computation checks (factor-of-2 fix etc.) | Keep as correction/validation provenance | `CORRECTED` + `KNOWN / REFRAMED` | OCP noncanonical appendix or archived validation note |

## Demote (stay outside OCP theorem spine)

| Section/theme | Demotion reason | Destination |
|---|---|---|
| “Horizon obstruction theorem” as core novelty | largely reframing of known semiclassical accessibility statements | OCP exploratory physics note only |
| Page-time-as-rho-phase-transition strong language | interpretation > theorem | OCP exploratory note with `OPEN` tags |
| KN near-null direction as structural invariant claim | currently numerical/model-dependent | OCP exploratory diagnostics, not theorem spine |

## Move/Route toward SDS-side or external spin-off

| Section/theme | Why not OCP core | Proposed home |
|---|---|---|
| Broad BH thermodynamic synthesis narratives | thermodynamic identity framing is closer to SDS thematic program | SDS side-note / companion repo |
| Extremality as “ground-state” architecture language | conceptually broad and not OCP-theorem-backed | SDS exploratory note |
| Multi-entropy unification ambition | mostly known physics + exploratory packaging | external spin-off manuscript draft |

## Cut from promotion queue (for now)

| Claim class | Why cut now |
|---|---|
| Universal BH Fisher conservation identity | currently `OPEN`; no proof or robust evidence |
| Any “new BH foundation via OCP” framing | unsupported and high literature-collision risk |
| Cosmological tension resolution claims | no theorem-grade resolution demonstrated |

## Immediate labeling actions

1. All retained BH/cosmology material must carry one of: `KNOWN / REFRAMED`, `VALIDATED / NUMERICAL ONLY`, or `OPEN`.
2. No BH/cosmology item should be marked as OCP core theorem without independent branch-level proof pressure in this repo.
3. Any future integration must include explicit literature-overlap language.
