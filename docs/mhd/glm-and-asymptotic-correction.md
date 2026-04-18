# GLM and Asymptotic Correction

GLM divergence cleaning belongs to the asymptotic branch, not the exact projector branch.

Projection cleaning removes disturbance by one explicit projector step on compatible classes. GLM introduces an auxiliary field and suppresses divergence error through evolution and damping over time. This is a different correction architecture and should be labeled accordingly.

In OCP language, the protected target and disturbance interpretation is still meaningful, but the recovery law is asymptotic. That is why GLM is retained as a continuous suppression example and not promoted as one-step exact correction.

Repository tests support the decay interpretation on declared setups; they do not upgrade GLM to an exact theorem.
