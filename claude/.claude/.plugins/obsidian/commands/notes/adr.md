---
description: Create ADR (Architecture Decision Record) note
argument-hint: [topic]
---

Create a structured Architecture Decision Record.

Decision topic: $ARGUMENTS

## Steps

1. Read `/home/maxime/NOTES/CLAUDE.md` for:
   - ADR template and format
   - Decisions folder location
   - Numbering scheme

2. Get additional context from conversation if needed (context, options considered)

3. Determine ADR number (find last ADR and increment, or use date-based)

4. Create structured ADR note:
   ```markdown
   ---
   type: decision
   status: proposed
   date: YYYY-MM-DD
   tags: [adr, <project-tag>]
   ---

   # ADR-NNN: <Title>

   **Status**: Proposed | Accepted | Deprecated | Superseded
   **Date**: YYYY-MM-DD
   **Deciders**: <Who made/approved this>
   **Project**: [[Project Name]]

   ## Context

   What is the issue we're facing? What factors are driving this decision?

   ## Decision

   What are we deciding to do?

   ## Options Considered

   ### Option 1: <Name>
   - Pros:
   - Cons:

   ### Option 2: <Name>
   - Pros:
   - Cons:

   ## Rationale

   Why did we choose this option over others?

   ## Consequences

   ### Positive
   - What benefits do we expect?

   ### Negative
   - What trade-offs are we accepting?

   ### Neutral
   - Other implications

   ## Implementation Notes

   <Technical details if relevant>

   ## References

   - Links to related notes, docs, discussions
   ```

5. Save to `Decisions/ADR-NNN-<title>.md` or `Projects/<project>/Decisions/`

6. Add reference to today's daily note and relevant project note

Use ADR format. Number sequentially. Status: proposed/accepted/deprecated/superseded. Link to related decisions if superseding.
