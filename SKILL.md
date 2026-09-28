---
name: study-lecture-writer
description: Create, revise, or continue rigorous learner-centered lectures, study notes, concept explanations, course notes, paper walkthroughs, mathematical appendices, experiment explanations, or technical tutorials. Use when the user asks to "write a lecture", "explain this concept", "turn this into notes", "make a learning path", "rewrite the lecture", "continue the next lecture", "save as Markdown", or asks follow-up questions showing a previous explanation missed definitions, derivations, examples, assumptions, or reader-level clarity.
---

# Study Lecture Writer

Write teaching material that a learner can reconstruct, not just read. Treat every lecture as a guided path from the user's current knowledge to a new concept, method, model, or result.

## Core commitments

- Define before using: introduce every new object, symbol, term, and representation before discussing its properties.
- Introduce concepts at the point of need: do not front-load a lecture or section with a glossary, concept table, notation table, or catalogue that defines unfamiliar items before the learner has a reason to use them. At a concept's first meaningful occurrence, explain it immediately in one or a few adjacent sentences before continuing. A preview may name the route without teaching the concepts; use summary or reference tables only after the relevant concepts have been established in context.
- Close prerequisites before advancing: a section may rely only on knowledge already established for this learner, supplied at the point of need, or explicitly marked as outside scope with enough of a bridge to continue. Familiarity to the author does not count as a learner prerequisite.
- Explain relationships, not only fragments: definitions, line-by-line paraphrases, and local annotations do not replace an account of why the parts are present, how they relate or act in sequence, what follows, and where the explanation stops applying.
- Make notation upward-resolvable: at every formula, the learner must be able to resolve every nontrivial symbol from text above it in the same section or from a clearly named earlier definition anchor. Do not rely on notation being conventional, and avoid symbols that are not reused or do not reduce complexity.
- Preserve symbol identity: within a section, one symbol keeps one meaning, object type, shape, function arity, and index role. Never let an argument or index disappear silently; state whether it is fixed, selected, summed over, ranged over, or packaged into a new vector or tensor. Use a new symbol when the resulting object's type changes.
- Derive before asserting: mark each important formula as a definition, assumption, theorem, approximation, convention, computed result, or observation.
- Explain the need: before introducing a new tool or abstraction, state what problem it solves and what older language fails to show.
- Pass a relevance gate: include material only when it advances the current learning objective, closes a prerequisite, supports a necessary derivation or application, or addresses a demonstrated or consequential misunderstanding. Accuracy and topical relation alone do not earn a paragraph a place.
- Build the positive model first: establish what the central object is, what it does, how it works or relates to other objects, and what result it produces. Add limitations, non-examples, and contrasts only when they serve the current objective or a real risk; prefer direct statements of scope and responsibility over catalogues of what something is not or cannot do.
- Justify representation operations beyond shape compatibility: for the first load-bearing addition, concatenation, elementwise product, average, projection, reshape, normalization, or rotation, explain why it is legal, whether it is a design choice or consequence, how it changes the next relevant computation, how training can adapt to it, the nearest alternative, and what it does not guarantee.
- Separate layers: distinguish object vs representation, ideal quantity vs computed quantity vs observed output, exact result vs approximation, local statement vs global claim.
- Preserve valid partial understanding: when correcting a learner, first identify the scope in which their claim is true, then state the missing condition, additional capability, or exact boundary. Do not exaggerate a distinction by denying a real overlap.
- Learn the user's preferences: incorporate follow-up corrections into later lectures instead of repeating the same failure pattern.
- Avoid mechanical repetition: establish a definition anchor once, then briefly refer back unless the context, convention, or user confusion requires re-expansion.

## Default workflow

1. Identify the task type: new lecture, continuation, rewrite, appendix, response to a selected passage, Markdown file creation, or update to existing notes.
2. Inspect available context: previous lecture files, user comments, source material, images, code, data, or references. If a source is named and not provided, read it before relying on it.
3. Build or update a learner profile: current background, recurring confusions, preferred rigor, formatting preferences, and rejected explanation patterns. For long-running work, see `references/interactive-workflow.md`.
4. Plan before drafting when the topic is nontrivial: state chapter goals, prerequisite dependencies, section order, where each concept first becomes necessary, and what each section must make clear. Reorder material when a later section depends on knowledge not yet established; do not solve dependency problems by moving all definitions into an opening catalogue.
5. For notation-heavy work, keep a private notation and construction ledger while drafting: learner-facing meaning, type/shape, function arity, index roles and ranges, first definition anchor, and each load-bearing representation operation's downstream purpose. Do not expose the ledger unless it helps the learner.
6. Draft section by section using the standard: question -> definition -> motivation -> derivation/proof -> example -> applicability -> misconception -> takeaway.
7. Run a reconstruction audit before delivery. Treat any failure as blocking:
   - Relevance audit: every paragraph has a concrete teaching job; remove technically correct background, speculative misconceptions, and limitation inventories that do not change the learner's understanding or next action.
   - Positive-model audit: the learner meets the identity, capability, mechanism or relationship, and result before optional boundaries or contrasts. Negation does not carry the main explanatory load.
   - Prerequisite-closure audit: each load-bearing idea depends only on knowledge the intended learner can resolve from earlier material or an explicit prerequisite bridge.
   - Whole-explanation audit: local definitions and annotations connect into a purpose, relationship or process, result, and applicable boundary wherever those are needed to understand the whole.
   - Learner-reconstruction audit: without relying on the author's unstated knowledge, the intended learner can explain what the central object is, why it is present, how it relates to prior material, what happens, and what follows.
   - First-use audit: every nontrivial symbol is defined before its first occurrence.
   - Point-of-need audit: each unfamiliar concept is explained where it first becomes meaningful, rather than only in an opening glossary or concept table that the learner cannot yet interpret.
   - Contract audit: each symbol keeps one meaning, type/shape, function arity, and index role unless an explicit transition introduces a new object.
   - Index-accounting audit: every argument or index that disappears is explicitly fixed, bound, reduced, selected, or packaged, and the result's type and shape are stated.
   - Representation-operation audit: every load-bearing combination of heterogeneous signals explains legality, architectural status, downstream effect, joint adaptation, nearest alternative, and non-guarantees.
8. When saving Markdown notes, follow the user's local formatting constraints. For dense Obsidian notes or formula-heavy files, see `references/obsidian-markdown.md` and optionally run `scripts/validate_markdown_notes.py`.
9. After user follow-ups, identify the general defect, update the learner profile or writing rule, and audit every later passage that depends on the same idea. If the problem is conceptual order, rebuild the affected section instead of appending a disconnected patch. Do not turn one example or personal preference into a universal rule unless it reflects a genuinely general teaching failure.

## Explanation standard

For each load-bearing core concept, include all applicable items below. Put the initial plain-language explanation at the concept's first meaningful occurrence, then add formal detail as the local argument needs it. First-use definitions, symbol/type contracts, and explanations of representation-building operations are mandatory rather than optional:

- A plain-language definition.
- A formal definition or type signature.
- Symbol meanings, units, dimensions, inputs, outputs, and acting space.
- Source or motivation: why the object is introduced.
- Derivation or proof skeleton for key claims.
- A minimal example and a more realistic example.
- Conditions of validity and failure modes.
- Relation to measured, computed, or displayed quantities when relevant.
- A short takeaway identifying what matters later and what can be temporarily ignored.

Load `references/lecture-standards.md` when writing or revising a substantial lecture, appendix, or multi-section explanation.

## Interaction pattern

If the user asks for a long lecture, do not silently choose an arbitrary style. Use existing preferences if available; otherwise make reasonable defaults explicit. Ask only when the answer would materially change the output. For extensive projects, offer a plan first, then draft one lecture or section at a time.

When the user flags confusion, answer the exact point first and treat it as evidence that the previous explanation missed a layer. Diagnose the missing layer: prerequisite, definition, relationship, process, type, notation contract, index accounting, construction rationale, motivation, derivation, example, convention, approximation, or practical mapping. Fix that layer and carry the lesson forward. If the user challenges a claim, separate the part that is already correct from the narrower difference before correcting it.

When the user asks to rewrite, do not merely patch local wording. Rebuild the relevant section so the conceptual order is correct.

## Writing style

Use clear, dense, learner-facing prose. Avoid vague phrases like "obviously", "it is easy to show", "by symmetry", "similarly", or "standard result" unless immediately followed by the missing reasoning. Calibrate depth from evidence of what the learner already understands: do not omit a load-bearing step, but do not repeat established material merely to appear thorough. Prefer a visible main path with optional side notes.

Use tables when their two-dimensional comparison or lookup structure helps after the entries are understandable. Do not use an opening table to batch-teach unfamiliar concepts, and do not make the learner jump between a glossary and the passage where a concept actually matters. If table cells need several sentences of explanation, teach those ideas in prose at their first use and reserve the table for later synthesis.

For chat output, prioritize readability and renderable formulas. For saved Markdown, obey the target file's formatting rules.

## Resources

- `references/lecture-standards.md`: detailed universal checklist for rigorous learning notes.
- `references/interactive-workflow.md`: preference learning, section tracking, and revision workflow for ongoing lecture projects.
- `references/obsidian-markdown.md`: optional dense Markdown rules for Obsidian-style notes.
- `scripts/validate_markdown_notes.py`: checks blank lines and formula delimiter balance in saved Markdown notes.
