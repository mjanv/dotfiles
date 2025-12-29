---
description: Create a Marp presentation with specified theme and topic
argument-hint: Optional topic or presentation title
---

# Create Marp Presentation

Create a professional Marp presentation about: $ARGUMENTS

## Requirements

1. Use Marp syntax with proper frontmatter
2. Choose appropriate theme (default/gaia/uncover) based on topic:
   - **default**: Clean, professional, general purpose
   - **gaia**: Modern, colorful, product/business presentations
   - **uncover**: Minimalist, elegant, academic/technical talks
3. Include 8-12 slides with logical flow:
   - Title slide (no pagination)
   - Agenda/overview
   - 5-8 content slides
   - Summary/conclusion
   - Q&A/contact slide
4. Use directives effectively (backgrounds, pagination, styling)
5. Save as `presentation.md` in current directory

## Style Guidelines

- One main idea per slide
- Use visual hierarchy with headings (`#` for titles, `##` for content slides)
- Add relevant images/backgrounds where appropriate
- Keep text concise and readable (bullet points, not paragraphs)
- Include speaker notes as HTML comments if helpful

## Content Structure

For technical talks:
- Problem statement
- Solution approach
- Key concepts with examples
- Implementation details
- Results/benefits

For business presentations:
- Executive summary
- Current situation/challenges
- Proposed solution
- Timeline/roadmap
- Next steps

## Export Instructions

After creating the presentation, inform the user:
- Location of the `.md` file
- How to export: `marp presentation.md -o presentation.html` (HTML)
- Or: `marp presentation.md -o presentation.pdf` (PDF)
- Or use Marp for VS Code extension for live preview