# Kept Versus Rejected CFD Bridges

## Kept

### 1. Periodic incompressible projection
- status: **KEPT / EXACT FIT**
- reason: it uses a real projector onto the divergence-free velocity class and matches the exact projector branch cleanly

### 2. Projection methods as the correction step inside incompressible solvers
- status: **KEPT / EXACT FIT AT THE CORRECTION STEP**
- reason: the correction step itself is a real exact operator when it realizes the correct projector, even though the full solver includes additional approximation layers

### 3. Bounded-domain projection with a domain-compatible Hodge projector
- status: **KEPT / CONDITIONAL**
- reason: this is the right direction for a stronger future CFD branch, but the repo does not yet prove the full bounded-domain theory

### 4. CFD versus MHD projection comparison
- status: **KEPT / STRUCTURAL COMPARISON**
- reason: it compares real operator classes without pretending the governing physics are the same

## Rejected

### 1. Naive periodic-projector transplantation to bounded domains
- status: **REJECTED**
- reason: it removes divergence while violating the bounded protected class through boundary-normal mismatch

### 2. Divergence-only bounded recovery as an exact correction architecture
- status: **REJECTED / NO-GO**
- reason: distinct protected states can share the same divergence data, so divergence alone is not enough information for exact recovery

### 3. OCP as a theory of all CFD stabilization methods
- status: **REJECTED**
- reason: most CFD stabilization methods do not arrive with the protected/disturbance/operator structure needed here

## Bottom Line

The CFD extension is worth keeping, but only as a narrow lane centered on incompressible projection and its exact-versus-bounded-domain boundary.
