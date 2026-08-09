# Formalisation status

**State:** planned; no proof-assistant theorem has been checked.

The package contains a detailed Lean-oriented blueprint but no `lean-toolchain`,
Lake project, Lean source file, build receipt, or axiom audit. The manifest must
therefore record `formalisation.status` as `planned`.

The highest-value first kernel is the ring-level block-composition lemma, the
self-contained two-factor complementary-minor identity, the all-factor
Delta-times-Plucker induction, and the arbitrary multi-border contraction over
the integers. Weighted graph minors and the Smith arithmetic form a second
layer. Geometric quotient, affine-slice, Keller, and Hessian statements are
outside the proposed first formal kernel.

See `FORMALIZATION_BLUEPRINT.md` for theorem interfaces, dependencies, sign
conventions, completion gates, and the proposed Mathlib pin. A future clean
build would certify only the encoded statements under its audited axioms; it
would not establish novelty, independent reproduction, or correspondence with
the prose without a separate statement audit.
