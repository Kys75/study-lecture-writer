# Obsidian Markdown output rules

Use these only when saving lecture notes into a dense Markdown knowledge base or when the user requests this style. Chat output should remain readable and need not follow these density rules.

## Dense note formatting

- Avoid unnecessary blank lines.
- Keep headings, paragraphs, lists, and formula blocks compact.
- Use consistent heading levels.
- Keep formulas closed and renderable.
- Do not leave placeholder sections.
- Do not dump unrelated auxiliary commentary into the note.

## Formula conventions

- Use the formula delimiter style already used by the target file.
- For display math in Markdown files, prefer paired display delimiters that the user's renderer supports.
- Check that display delimiters are balanced before finishing.

## File update behavior

- Preserve existing user content unless asked to rewrite it.
- If adding a new lecture, keep naming consistent with existing notes.
- If revising a lecture, address the conceptual defect, not only the local wording.

## Validation

After writing or editing a saved Markdown note, run `scripts/validate_markdown_notes.py <file>` from this skill when appropriate. Use `--allow-blank-lines` if the target document intentionally uses spaced formatting.
