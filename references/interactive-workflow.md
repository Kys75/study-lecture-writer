# Interactive workflow for long-running lecture projects

Use this when the user is building a series of lectures, repeatedly asks follow-up questions, or wants notes saved and improved over time.

## 1. Read globally before writing locally

Before drafting a new lecture in an ongoing sequence, inspect the existing plan, previous notes, user corrections, and any writing-rule file. The goal is to avoid repeating old mistakes and to keep terminology consistent.

## 2. Maintain a learner profile

Track these preferences mentally or in a project note when the project is long:

- Current background and comfortable prerequisites.
- Demonstrated understanding: what the learner can already restate, distinguish, predict, or apply without prompting.
- Current reading or stopping point when the material is being studied over multiple sessions.
- Desired rigor and tolerance for formalism.
- Preferred output format: chat, Markdown file, dense notes, figures, worked examples.
- Recurring pain points: missing definitions, definitions front-loaded in a concept table instead of placed at first use, skipped derivations, unclear symbols, silent type/arity/index changes, unexplained representation operations, weak examples, unmarked approximations, bad figures, over-compressed notation, irrelevant caveats, or explanation dominated by negative framing.
- Formatting constraints for saved files.

Do not turn this into a visible bureaucratic process unless useful; use it to improve later writing.

## 3. Use stable sections

For long notes, give sections stable titles or numbers so later corrections can target them. When the user asks a follow-up about a passage, update the conceptual rule behind the issue and, if requested, revise the section rather than appending a disconnected fix.

## 4. Let the user steer depth

Use prior questions, correct restatements, objections, and mistakes as evidence of the learner's current depth. Begin with the exact gap instead of restarting the whole topic, and do not repeat established material or pre-emptively catalogue possible misconceptions merely to appear complete. When multiple depths are plausible, offer a concise choice only if it materially affects the result; otherwise use the learner profile and mark optional advanced material clearly.

## 5. Learn from corrections

A user correction usually reveals one of these defects:

- Technically correct material included without a concrete role in the current learning path.
- A concept framed mainly through what it is not or cannot do before its positive model is established.
- Missing prerequisite or a section ordered before its dependencies.
- Unfamiliar concepts batch-defined in an opening glossary or table before their roles become meaningful, instead of explained locally at first use.
- Undefined object.
- Locally explained fragments that never form a coherent relationship or process.
- Purpose, source, result, or applicable boundary left implicit.
- Symbol introduced as assumed convention rather than learner knowledge.
- Symbol meaning, type, shape, function arity, or index role changed silently.
- Argument or index disappeared without an explicit binding or packaging step.
- Unclear acting space.
- Dimensional legality was mistaken for an explanation of why an architectural operation is meaningful.
- Joint training, downstream effect, nearest alternative, or non-guarantee of a representation choice was omitted.
- Missing derivation.
- Formula status not labeled.
- Approximation not stated.
- Example too trivial.
- Practical quantity confused with ideal quantity.
- Visual or analogy misleading.
- Repetition too mechanical.

Convert the defect into a reusable writing habit at the right level of generality. Do not encode a single example or personal preference as a universal requirement unless the same reasoning applies beyond that instance.

## 6. Handle disagreement precisely

When the learner challenges an explanation, do not jump directly to a categorical correction. First identify what their claim says, then separate:

- The scope in which it is already true.
- The missing condition, extra capability, or narrower distinction.
- The conclusion that actually changes.

This preserves valid partial understanding and prevents a useful distinction from being overstated into a false opposition.

## 7. Preserve the user's learning style

The goal is not to impose a generic textbook voice. If the user prefers dense notes, rigorous proofs, conversational explanations, diagrams, or step-by-step algebra, adapt consistently. Keep what works and stop proposing patterns the user repeatedly rejects.

## 8. Revision behavior

When improving an earlier lecture, do not only patch the sentence the user complained about. Check whether earlier prerequisites, definitions, relationships, notation contracts, section order, examples, assumptions, or representation choices must be reorganized so the issue does not recur. Re-run the reconstruction audit on the revised section and every later passage that depends on the same concept, not only passages that repeat the same wording or notation.
