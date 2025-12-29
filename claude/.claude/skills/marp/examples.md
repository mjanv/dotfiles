# Marp Presentation Examples

Complete templates and advanced patterns for Marp presentations.

## Example 1: Simple Tech Talk

```markdown
---
marp: true
theme: default
paginate: true
_paginate: false
---

# Building Scalable APIs

## Best Practices and Patterns

John Doe
December 2025

---

## Agenda

1. Introduction to API Design
2. RESTful Principles
3. Performance Optimization
4. Security Considerations
5. Q&A

---

## RESTful Principles

- **Resource-based**: URLs represent resources, not actions
- **HTTP verbs**: GET, POST, PUT, DELETE for operations
- **Stateless**: Each request contains all needed information
- **HATEOAS**: Hypermedia as the engine of application state

---

![bg right:40%](https://via.placeholder.com/400)

## Performance Tips

- Implement caching strategies
- Use pagination for large datasets
- Optimize database queries
- Compress responses (gzip)

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Questions?

Contact: john@example.com

```

## Example 2: Professional Presentation (Gaia Theme)

```markdown
---
marp: true
theme: gaia
paginate: true
_paginate: false
header: 'Q4 Product Roadmap'
footer: 'Confidential • 2025'
---

<!-- _header: '' -->
<!-- _footer: '' -->

# Q4 Product Roadmap

Accelerating Growth Through Innovation

**Product Team**
December 2025

---

## Executive Summary

Our Q4 roadmap focuses on three strategic pillars:

1. 🚀 **User Experience** - Streamlined onboarding
2. 📊 **Analytics** - Advanced reporting dashboard
3. 🔐 **Enterprise** - SSO and compliance features

---

## User Experience Improvements

<!-- _backgroundColor: #e3f2fd -->

### Onboarding Flow Redesign

- Interactive tutorial (Week 1-2)
- Contextual help tooltips (Week 3)
- Progress tracking (Week 4)

**Expected Impact**: 40% reduction in time-to-value

---

![bg](https://via.placeholder.com/1280x720/2196f3/ffffff?text=Analytics+Dashboard)

---

## Analytics Dashboard

**Features**:
- Real-time metrics visualization
- Customizable report builder
- Export to PDF/Excel
- Scheduled email reports

**Timeline**: 6 weeks
**Resources**: 2 engineers, 1 designer

---

## Enterprise Features

| Feature | Status | Release |
|---------|--------|---------|
| SAML SSO | In Progress | Week 42 |
| SCIM Provisioning | Planning | Week 45 |
| Audit Logging | Complete | Week 40 |
| SOC 2 Compliance | In Progress | Week 48 |

---

<!-- _class: lead -->

# Next Steps

**Weekly syncs start next Monday**

Engineering kickoff: December 15

```

## Example 3: Educational Content (Uncover Theme)

```markdown
---
marp: true
theme: uncover
paginate: true
math: katex
---

# Linear Algebra

**Matrices and Transformations**

---

## What is a Matrix?

A rectangular array of numbers arranged in rows and columns.

$$
A = \begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23}
\end{bmatrix}
$$

---

## Matrix Multiplication

For matrices $A$ (m×n) and $B$ (n×p):

$$
(AB)_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}
$$

**Key property**: Matrix multiplication is **not commutative**

$AB \neq BA$ (in general)

---

![bg left:30%](https://via.placeholder.com/400)

## Applications

- Computer graphics
- Machine learning
- Quantum mechanics
- Economics modeling
- Network analysis

---

## Example: 2D Rotation

Rotating point $(x, y)$ by angle $\theta$:

$$
\begin{bmatrix}
x' \\
y'
\end{bmatrix}
=
\begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

---

<!-- _class: lead -->

# Practice Problems

See handout for exercises

```

## Example 4: Image-Heavy Presentation

```markdown
---
marp: true
theme: default
paginate: true
---

<!-- _paginate: false -->
![bg](hero-image.jpg)

# Travel Photography

## Capturing the Moment

---

![bg fit](landscape1.jpg)

---

![bg](landscape2.jpg)

## Rule of Thirds

Position key elements along imaginary grid lines

---

![bg left](portrait.jpg)

## Portrait Tips

- Natural lighting
- Focus on eyes
- Shallow depth of field
- Environmental context

---

<!-- Multiple backgrounds in grid -->
![bg](photo1.jpg)
![bg](photo2.jpg)
![bg](photo3.jpg)
![bg](photo4.jpg)

---

![bg right:60% fit](camera.jpg)

## Equipment

### Camera
- Full-frame DSLR
- 24-70mm lens
- Tripod

### Accessories
- ND filters
- Remote shutter
- Extra batteries

```

## Example 5: Advanced Custom Styling

```markdown
---
marp: true
theme: default
paginate: true
style: |
  section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
  }
  h1, h2 {
    color: #ffd700;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
  }
  a {
    color: #ffd700;
  }
  code {
    background: rgba(255,255,255,0.1);
    color: #ffd700;
  }
  section.lead {
    text-align: center;
    justify-content: center;
  }
---

<!-- _paginate: false -->
<!-- _class: lead -->

# Custom Styled Deck

Unique branding and visual identity

---

## Code Example

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

Recursion in action!

---

<!-- _backgroundColor: white -->
<!-- _color: #333 -->

## Light Slide Override

This slide breaks the gradient pattern for emphasis.

- Dark text on light background
- Better for detailed content
- Improved readability

---

<!-- _class: lead -->

# Thank You

Visit: **example.com**

```

## Example 6: Data Presentation

```markdown
---
marp: true
theme: gaia
paginate: true
header: 'Sales Report Q4 2025'
---

## Revenue Growth

<div style="font-size: 3em; text-align: center; margin: 2em 0;">
📈 +47%
</div>

Year-over-year increase

---

## Regional Performance

| Region | Revenue | Growth |
|--------|---------|--------|
| North America | $2.4M | +52% |
| Europe | $1.8M | +38% |
| Asia Pacific | $1.2M | +61% |
| Latin America | $0.6M | +29% |

---

## Top Products

1. **Enterprise Suite** - $1.8M
2. **Professional Plan** - $1.4M
3. **Starter Pack** - $0.9M
4. **Add-ons** - $0.5M

---

![bg right:50%](chart-image.png)

## Key Insights

- Enterprise segment growing fastest
- Strong retention (94%)
- International expansion success
- Product-market fit validated

```

## Tips for Each Example

### Tech Talk
- Use code blocks with syntax highlighting
- Keep technical details concise
- Include diagrams where helpful
- End with resources/links

### Professional Presentation
- Corporate branding in headers/footers
- Tables for structured data
- Status indicators (emojis, colors)
- Clear timeline information

### Educational Content
- Math typesetting with KaTeX
- Progressive concept building
- Visual aids on side panels
- Practice exercises at end

### Image-Heavy
- `![bg fit]` for optimal image display
- Minimal text over images
- Use `![bg left/right]` for split layouts
- Grid backgrounds for galleries

### Custom Styling
- Define brand colors in frontmatter
- Use CSS gradients and shadows
- Override styles per slide as needed
- Maintain readability

### Data Presentation
- Tables for structured comparison
- Large numbers for key metrics
- Charts as background images
- Regional/categorical breakdowns