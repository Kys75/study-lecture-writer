# Lecture standards

Use this checklist for substantial study notes, lectures, appendices, and concept explanations.

## 1. Start from a problem and pass a relevance gate

Open each section by stating the problem it solves. The reader should know why the next object, formula, or method is being introduced before seeing it.

Every paragraph must earn its place by doing at least one concrete teaching job: advancing the stated objective, closing a prerequisite, supporting a necessary derivation, enabling an application, or addressing a misunderstanding that is observed or consequential. A statement can be accurate and related to the topic yet still be irrelevant at this point in the learning path.

Remove background, caveats, non-examples, and lists of limitations when their omission would leave the learner equally able to understand and use the central idea. Completeness means including what the learning path requires, not inventorying everything that could be said.

## 2. Close prerequisites and establish new objects

Before using a concept, determine what the intended learner must already know to understand its role. Each prerequisite must be established earlier, supplied at the point of need, or explicitly placed outside scope with enough of a bridge for the reader to continue. A concept being conventional or familiar to the author does not establish it for the learner.

Place each new concept's explanation where the concept first becomes necessary. Introduce the name together with one or a few adjacent sentences saying what it means here, why it has entered the discussion, and how it connects to the current problem; then provide any formal detail the local argument needs. Do not open a lecture or section with a glossary, concept table, notation table, or component catalogue that batch-defines unfamiliar items before the learner has a use context for them. Such a table may summarize or compare concepts after they have been established, or serve as a reference when the intended learner already knows its entries, but it must not carry the first explanation.

Do not explain one unfamiliar object only through other unexplained objects. A definition is incomplete if it supplies a label but leaves the object's learner-facing role, source, or necessary relationships implicit.

Establish a positive model before introducing boundaries: state what the object is, what role or capability it has, how it works or relates to prior objects, and what result follows. Add a limitation, contrast, or non-example only when it changes the learner's use of the idea, answers a demonstrated confusion, or prevents a consequential error. Prefer a direct statement of scope or division of responsibility to a repeated sequence of "is not," "cannot," and "does not."

For every new object, state what it is and how it acts. Use this template when useful:

- Name and symbol.
- Object type.
- Inputs and outputs.
- Space, domain, codomain, basis, or units.
- Components or representation.
- Meaning in words.

A symbol counts as established only when its learner-facing meaning and role have been stated before first use. Do not rely on conventional notation the learner has not used. Prefer readable names such as `vocab_size` before compact set notation such as \(|\mathcal V|\), and introduce the compact notation only when it will be reused or set operations matter.

## 3. Enforce notation contracts

For formula-heavy work, maintain a private notation ledger. Record each symbol's meaning, object type, shape or range, function arity, index roles, and first definition anchor.

Within a section, do not silently change a symbol's:

- Meaning or object type, such as scalar to vector.
- Shape or acting space.
- Function arity, such as \(f(x,y)\) to \(f(x)\).
- Index role, such as sequence position to feature coordinate.

If a component formula becomes a vector or tensor, use distinct notation and show the packaging operation. For example, first define one scalar component:

\[
c(p,k)\in\mathbb R,
\]

then define the complete vector:

\[
\mathbf c_p
=
[c(p,0),c(p,1),\ldots,c(p,d-1)]^\top
\in\mathbb R^d.
\]

State that \(k\) is traversed over all component indices; it has not vanished. Apply the same rule whenever an index is fixed, selected, summed over, reduced, or broadcast.

## 4. Mark formula status

Label important formulas as one of:

- Definition.
- Assumption or model choice.
- Convention.
- Theorem.
- Consequence or corollary.
- Approximation.
- Computed result.
- Empirical or observed relation.

Do not let the reader guess whether a formula is being defined or derived.

## 5. Derive key results

For each central conclusion, provide the derivation or a proof skeleton. A proof skeleton must include the starting point, the transformation steps, the reason each step is legal, and the final comparison or interpretation.

Avoid unsupported transitions such as "clearly", "similarly", "one obtains", "by standard arguments", or "it can be shown". If space is limited, say exactly what is being omitted and why.

## 6. Explain abstractions and relationships by translation

When introducing a new representation, first write the familiar version. Then map old objects to new objects, old operations to new operations, and old conclusions to new conclusions. This prevents new notation from becoming a black box.

Local explanations do not automatically compose into an explanation of the whole. For each central construction, make the applicable parts of this chain recoverable: why it is introduced, where its parts come from, how the parts relate or act in sequence, what result follows, and what the account does not establish. Use the chain as an audit, not as a rigid paragraph template. If a learner can paraphrase each fragment but cannot reconstruct the overall relationship or process, the explanation is incomplete.

## 7. Justify architectural representation choices

Shape compatibility proves only that an operation can be computed. It does not explain why the operation is useful or meaningful.

For the first load-bearing use of addition, concatenation, elementwise multiplication, averaging, projection, reshaping, normalization, rotation, or another representation-building operation:

1. State the participating objects, types, and shapes, and why the operation is well-typed.
2. Label the formula as a definition, architectural choice, or derived consequence.
3. Substitute the result into the next relevant learned computation and expand one step to show its functional effect.
4. Explain which quantities are fixed or learned and how joint training can adapt to the construction.
5. Compare the nearest plausible alternative and its cost or expressive tradeoff.
6. State non-guarantees and failure modes, including information mixing or loss, collisions, scale dominance, non-invertibility, or extrapolation limits when relevant.

"The shapes match" and "the model learns it" are not sufficient explanations by themselves.

## 8. Use layered examples

Give at least two examples for core concepts:

- Minimal example: checks the definition with the smallest nontrivial case.
- Nontrivial example: shows how the concept behaves in a realistic calculation or application.

Add a counterexample or failure case when the concept is often overgeneralized.

## 9. Separate levels of reality

Keep these layers distinct:

- Ideal mathematical object.
- Model representation.
- Approximate formula.
- Numerical implementation.
- Experimental or practical observable.
- Displayed figure, fitted parameter, or software output.

Whenever moving between layers, state the map and the information lost or added.

## 10. State assumptions and failure modes

Every model or approximation needs its assumptions, small parameters, kept terms, discarded terms, and expected failure modes. Explain what would need to change when the assumptions fail.

## 11. Control repetition

The first explanation of a concept should be complete. Later uses should briefly recall the definition anchor instead of repeating the full derivation. Re-expand only when a convention changes, a new role appears, or the user asks a question that shows the anchor was insufficient.

Calibrate depth from evidence of the learner's current understanding. Start at the exact missing layer and expand only as far as needed to restore the dependency chain. More words do not repair a missing relationship, and brevity does not justify skipping a load-bearing step.

## 12. Run a reconstruction audit

Before delivery, read the lecture as the intended learner and treat these failures as blocking:

- A paragraph is present mainly because it is technically true or adjacent to the topic, but removing it would not weaken the intended learning outcome.
- A central object is introduced primarily through denials, exclusions, or speculative misconceptions before the learner receives a positive account of its identity, capability, relationship, or result.
- A section relies on prerequisite knowledge that has neither been established nor bridged.
- An unfamiliar concept receives its only substantive explanation in a front-loaded glossary or table, separated from the passage where its role first becomes meaningful.
- A new unfamiliar term, symbol, analogy, or category is used as the sole explanation of another unfamiliar object.
- Each fragment can be paraphrased locally, but the purpose, relationship, process, result, or boundary of the whole cannot be reconstructed.
- A formula contains a nontrivial symbol that cannot be resolved by reading upward.
- A symbol changes meaning, type, shape, arity, or index role without an explicit transition.
- An argument or index disappears without a stated binding, reduction, selection, or packaging operation.
- A component-level definition becomes a vector or tensor without an assembly equation.
- A load-bearing architectural operation is justified only by compatible shapes or by saying the model learns it.

Scan words such as "just", "simply", "directly", "combine", and "obviously"; if they cross a conceptual step, replace them with the missing explanation.

Then close the source and test whether the intended learner could answer, at the depth relevant to the section:

- What is the central object or claim?
- Why is it introduced here?
- What earlier knowledge does it depend on, and how is it connected?
- What relationship, mechanism, or sequence produces the result?
- What conclusion follows, and under what conditions or boundaries?
- Could the learner use the explanation to predict or work through one nearby case rather than merely recognize the original wording?

If an answer depends on knowledge present only in the author's head, revise the section.

## 13. Separate validation lenses

Evaluate the work through distinct lenses:

- Correctness: the facts, derivations, and claims are accurate.
- Self-consistency: terms, symbols, assumptions, levels, and conclusions do not drift.
- Learnability: the intended learner can reconstruct the dependencies and central relationship without hidden author knowledge.
- Presentation reliability: the intended format preserves the relationships being communicated instead of depending on fragile spacing, rendering, or unstated visual conventions.

A mechanical validator, style check, or successful rendering proves only the invariant it checks. None of these lenses can substitute for the others.

## 14. End with takeaways

End each major section with:

- What was defined.
- What was derived.
- What conditions were used.
- What will be reused later.
- What details can be temporarily ignored.
