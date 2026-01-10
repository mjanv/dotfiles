---
description: Answer a query with relevant notes, formatted for sharing in chat
argument-hint: [query]
---

Answer the provided query using vault knowledge, formatted for chat sharing.

Query: $ARGUMENTS

## Steps

1. Read `/home/maxime/NOTES/CLAUDE.md` for vault structure

2. Search vault for relevant information:
   - Grep for key terms from query (case-insensitive)
   - Search in project notes, decisions, learnings, daily notes
   - Check for wikilinks and tags related to query
   - Prioritize: ADRs, project docs, recent learnings, implementation notes

3. Read top 10-15 most relevant notes

4. Synthesize answer from vault knowledge:
   - Answer the specific question asked
   - Use information from notes to support answer
   - Include technical details, decisions, or context from vault
   - Cite sources if relevant (can mention note names)

5. Format for chat sharing:
   - **Concise**: Get to the point quickly
   - **Clear**: Use simple language, avoid jargon
   - **Structured**: Use bullets or short paragraphs
   - **Professional**: Colleague-friendly tone
   - **Shareable**: Ready to copy-paste to Slack/Teams/Discord
   - **No markdown headers**: Use bold for emphasis instead

## Output Format

```
[Direct answer in 1-2 sentences]

[Supporting details if needed]:
• Point 1
• Point 2
• Point 3

[Additional context or caveats if relevant]
```

Keep it chat-length (3-8 lines max). Focus on actionable, accurate information. If information is missing or uncertain, say so clearly.
