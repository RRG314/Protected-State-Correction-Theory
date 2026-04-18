# Restricted Flow Recoverability

This note states the recoverability criterion used in restricted CFD-style linear families.

For `x = Fz`, record `y = OFz`, and target `LFz`, exact target recovery from the record exists if and only if

$$
\operatorname{row}(LF) \subseteq \operatorname{row}(OF)
$$

or equivalently `ker(OF) ⊆ ker(LF)`.

The point is structural, not amount-only: recoverability is controlled by compatibility between target and record geometry on the declared family. Equal rank or equal measurement count does not settle the question.

This criterion is branch-limited and should not be misread as a universal CFD observability theorem.
