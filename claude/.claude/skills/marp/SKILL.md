---
name: marp
description: Creates professional presentation slides using Marp (Markdown Presentation Ecosystem). Use when user asks to create a presentation, slides, slide deck, or mentions Marp.
---

# Marp Presentation Creation

Create professional presentation slides using Marp, which converts Markdown into beautiful HTML/CSS/PDF presentations.

## Core Syntax

### Basic Structure

```markdown
---
marp: true
theme: default
paginate: true
---

# Title Slide

---

## Regular Slide

Content here

---

## Another Slide

More content
```

**Key Points:**
- Use `---` (horizontal ruler) to separate slides
- First `---` block contains YAML frontmatter with global directives
- Each subsequent `---` creates a new slide
- Based on CommonMark Markdown specification

## Directives

### Global Directives (Apply to entire deck)

Define in YAML frontmatter at the start:

```yaml
---
marp: true
theme: default          # Built-in: default, gaia, uncover
size: 16:9              # Aspect ratio (16:9, 4:3)
paginate: true          # Show page numbers
header: 'Header text'   # Deck-wide header
footer: 'Footer text'   # Deck-wide footer
style: |                # Custom CSS
  section {
    background-color: #fff;
  }
headingDivider: 2       # Auto-split at heading level
math: katex             # Math typesetting library
title: 'Presentation Title'
author: 'Author Name'
---
```

### Local Directives (Apply to specific slides)

Use HTML comments for slide-specific settings:

```markdown
<!-- _paginate: false -->
# Title Slide
(no page number on this slide)

---

<!--
_backgroundColor: #123456
_color: white
-->
## Slide with Custom Colors
```

**Scoped vs Persistent:**
- `_directive` (with underscore) = applies ONLY to current slide
- `directive` (no underscore) = applies to current and ALL subsequent slides

### Common Local Directives

| Directive | Purpose | Example |
|-----------|---------|---------|
| `paginate` | Show page number | `<!-- paginate: true -->` |
| `header` | Slide header | `<!-- header: 'Section 1' -->` |
| `footer` | Slide footer | `<!-- footer: '' -->` (reset) |
| `class` | CSS class | `<!-- class: lead -->` |
| `backgroundColor` | Background color | `<!-- _backgroundColor: #e1f5fe -->` |
| `backgroundImage` | Background image | `<!-- backgroundImage: url('img.jpg') -->` |
| `color` | Text color | `<!-- _color: #333 -->` |

## Built-in Themes

Marp includes three themes:

1. **default** - Clean, professional appearance
2. **gaia** - Modern design with accent colors
3. **uncover** - Minimalist presentation style

```yaml
---
theme: gaia
---
```

## Advanced Features

### Image Syntax

```markdown
![](image.jpg)                    # Regular image
![bg](background.jpg)             # Background image
![bg left](image.jpg)             # Split background (left)
![bg right:40%](image.jpg)        # Split background (right, 40% width)
![bg fit](image.jpg)              # Fit background
![bg contain](image.jpg)          # Contain background
![width:500px](image.jpg)         # Sized image
![height:300px](image.jpg)        # Height-specified image
```

### Multiple Backgrounds

```markdown
![bg](image1.jpg)
![bg](image2.jpg)
![bg](image3.jpg)
```

### Math Typesetting

Enable with `math: katex` in frontmatter:

```markdown
Inline math: $E = mc^2$

Block math:
$$
\int_0^\infty f(x)dx
$$
```

### Auto-Scaling

Text automatically scales to fit slides. Force specific sizes:

```markdown
<!-- _class: lead -->
# Large Centered Text
```

### Custom Styling

Inject CSS via `style` directive:

```yaml
---
style: |
  section {
    font-family: 'Arial', sans-serif;
  }
  h1 {
    color: #2196f3;
  }
---
```

## Workflow

1. **Create markdown file** (e.g., `presentation.md`)
2. **Add YAML frontmatter** with global directives
3. **Write content** using `---` to separate slides
4. **Export** to HTML, PDF, or PowerPoint using Marp CLI or VS Code extension

## Best Practices

- **One idea per slide**: Keep slides focused
- **Use headings**: `#` for title slides, `##` for content slides
- **Leverage directives**: Use `_paginate: false` on title/section slides
- **Background images**: Use `![bg fit]` for full-screen imagery
- **Split layouts**: Combine `![bg left]` with content on right
- **Consistent styling**: Define global styles in frontmatter
- **Test pagination**: Ensure page numbers appear where intended

## Common Patterns

### Title Slide

```markdown
<!-- _paginate: false -->
# Presentation Title

## Subtitle

Author Name
Date
```

### Section Divider

```markdown
<!-- _class: lead -->
<!-- _paginate: false -->
# Section Title
```

### Content Slide with Image

```markdown
![bg right:40%](image.jpg)

## Topic

- Point 1
- Point 2
- Point 3
```

### Two-Column Layout

```markdown
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">

<div>

### Left Column
- Item 1
- Item 2

</div>

<div>

### Right Column
- Item A
- Item B

</div>

</div>
```

## Output Formats

Export presentations using:

- **HTML**: Self-contained, works in any browser
- **PDF**: Shareable document format
- **PowerPoint**: PPTX for compatibility

## References

See [examples.md](examples.md) for complete presentation templates and advanced patterns.