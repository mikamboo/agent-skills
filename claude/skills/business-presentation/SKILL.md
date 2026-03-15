---
name: business-presentation
description: >
  Generate a complete, professional business project presentation (HTML/PDF) from a simple idea description.
  Use this skill whenever the user describes a business idea, project, or startup concept and wants a presentation,
  pitch deck, business plan document, or project dossier — even if they don't use those exact words.
  Trigger on phrases like: "create a presentation for my idea", "make a business plan for", "I have a business idea",
  "generate a project document for", "make a pitch for my project", or any description of a business concept
  followed by a request to produce a document.
---

# Business Presentation Skill

Turn any business idea description into a complete, professional HTML presentation
with executive summary, market analysis, financials, SWOT, risk matrix, and roadmap.

## Overview — What this skill produces

A single, self-contained **`.html` file** that:

- Opens in any browser and prints to PDF with Ctrl+P → "Save as PDF"
- Has a sticky navigation bar, gradient hero header, and sectioned layout
- Uses professional card grids, tables, KPI strips, SWOT matrix, timeline, and risk table
- **Includes data-driven charts and diagrams** (TAM/SAM/SOM funnel, revenue projection bar,
  investment breakdown donut, competitive positioning bars) — powered by Chart.js CDN
- Is fully themed to match the business sector
- CSS and charts are fully self-contained; Chart.js loads from CDN (requires internet on first open)

---

## Process

Follow these five steps in order.

---

### STEP 1 — Extract and assess information

Read `references/user-info-guide.md` to understand what to extract.

From the user's message, collect:

- Business concept and product/service offering
- Sector and geography
- Target customers
- Company/founder name (if any)
- Budget or investment context (if mentioned)
- Any specific numbers or differentiators stated
- Language of the description

**Extract silently** — do not bombard the user with questions yet.

---

### STEP 2 — Deep web research

**This step is mandatory.** Use `WebFetch` to gather real, current market data before
writing a single section. Shallow AI-generated estimates are not acceptable — ground
the document in actual sources.

**What to search for** (run multiple searches in parallel where possible):

| Topic                          | What to find                                                    |
| ------------------------------ | --------------------------------------------------------------- |
| Market size & growth           | TAM for the sector + country; CAGR; key statistics              |
| Competitive landscape          | Key players operating in the geography; recent news             |
| Regulatory / legal context     | Licences, permits, taxes specific to sector + country           |
| Trends & drivers               | Recent reports, news articles on sector dynamics                |
| Benchmark financials           | Typical margins, startup costs, revenue per unit for the sector |
| Success stories / case studies | Similar businesses that succeeded or failed, and why            |

**Search strategy:**

- Combine sector + geography in queries (e.g. "marché restauration rapide Cameroun 2024",
  "food delivery market West Africa size")
- Prioritise sources: industry reports, local news, statistical offices, trade associations,
  company websites of competitors
- Fetch Wikipedia or industry overview pages for quick sector context
- If a URL returns a redirect, follow it

**Handle search failures gracefully:** If a search returns no useful data, fall back to
your trained knowledge and clearly mark those numbers as **(est. — source: internal knowledge)**.
Never invent statistics without this disclaimer.

**Research output:** Before moving to Step 3, compile internally:

- 3–5 concrete market statistics with sources
- Names of 3–6 actual competitors in the geography
- 2–3 relevant regulatory requirements
- Sector margin benchmarks

---

### STEP 3 — Ask targeted questions (ONLY if critical data is missing)

After extraction and research, determine if any of these **critical** fields are truly missing
and cannot be inferred:

1. **Company or founder name** — needed for the document header
2. **Approximate launch budget** — if financial projections are central and no number was given

Ask **at most 2–3 questions in a single message**. Phrase them naturally:

> "Before I build your full presentation, just 2 quick questions to personalise it:
>
> 1. [question]
> 2. [question]"

Then wait for the answer before proceeding.

If the user says "just go ahead" or asks you to proceed without answering: use
defaults (`[Company Name]` for the name, and sector-typical estimates for financials).

---

### STEP 4 — Research and generate content

Read `references/sections-guide.md` for detailed guidance on each section.
Read `references/user-info-guide.md` for sector-specific financial benchmarks.

For each section, think as a senior business analyst who knows the sector well:

**Section content principles:**

- **Be specific and concrete.** Generic claims ("great growth potential") are worthless.
  Back everything with numbers, named competitors, named trends, specific actions.
- **Use your knowledge.** Apply real knowledge of the sector, geography, and market.
  If the business is in Libreville, describe the Gabonese market. If it's a SaaS startup,
  describe the digital landscape.
- **Mark estimates clearly.** When numbers are your estimates, add **(est.)** — this
  builds credibility rather than destroying it.
- **Size sections to their importance.** The financial section and market section deserve
  more depth than "conclusion". The executive summary must be tight.
- **Make the SWOT honest.** Real weaknesses and threats, not wishful thinking.
- **Make the risk table actionable.** Every risk must have a concrete mitigation.

**Colour theme:** Pick based on sector (see `references/sections-guide.md` → Colour Theme
Selection Guide). Override the `:root` CSS variables in the template accordingly.

---

### STEP 5 — Build and output the HTML file

Read `assets/template.html` as the **starting point** for the HTML output.

Replace every `__PLACEHOLDER__` token with generated content. Key tokens:

- `__COMPANY_NAME__` — brand or founder name
- `__PROJECT_TITLE__` — name of the project/concept
- `__PROJECT_TAGLINE__` — one-line elevator pitch
- `__LANG__` — `fr`, `en`, `es`, etc. based on detected language
- `__LOCATION__` — city or region
- `__SECTOR__` — sector label
- `__DATE__` — current date
- `__NAV_LINKS__` — `<a href="#section-id">Label</a><span class="sep">›</span>` for each section
- `__KPI1_VAL__` through `__KPI4_VAL__` / `__KPI1_LBL__` through `__KPI4_LBL__` — key metrics
- All section content tokens (see template comments)

**Sections are optional:** If a section has no meaningful content (e.g. no team info),
comment it out rather than leaving it blank. Re-sequence the numbers so they stay
consecutive.

**Nav links** must match the actual `id` attributes on the sections you include.
One nav link per included section. Use the section's title as the link text.

**After filling all content:**

1. Remove all remaining `__PLACEHOLDER__` tokens (if still present, replace with sensible defaults)
2. Remove template comments (the `<!-- Template: ... -->` blocks)
3. Verify chart `data` arrays in `<script>` blocks reflect the actual numbers used in the prose
4. Verify the HTML is valid and self-contained

**Output:** Write the finished HTML to a file named:
`[company-or-project-slug]-presentation.html`
in the current working directory (or one the user has indicated).

After writing the file, tell the user:

- The file path
- That it can be opened in any browser
- That to export as PDF: open in browser → Ctrl+P (or Cmd+P) → "Save as PDF" → adjust margins to "None" for best results

---

## Quality checklist

Before finalising, verify:

- [ ] All `__PLACEHOLDER__` tokens replaced
- [ ] Nav links match actual section IDs
- [ ] Section numbers are sequential
- [ ] Currency is consistent throughout the document
- [ ] Language matches the user's input language
- [ ] KPI strip has 4 real values with meaningful labels
- [ ] SWOT has ≥ 4 items per quadrant
- [ ] Risk table has ≥ 5 risks, each with a concrete mitigation
- [ ] Financial section has real numbers (even estimated) — no blank tables
- [ ] Colour theme matches the sector
- [ ] The hero subtitle / tagline is compelling, not generic
- [ ] **Market section includes TAM/SAM/SOM chart or market-size visualization**
- [ ] **Financial section includes revenue projection bar chart AND investment donut chart**
- [ ] **At least one other chart is present** (competitive bars, OPEX breakdown, growth forecast, etc.)
- [ ] **Chart data values are consistent with numbers in the prose**
- [ ] Web-sourced statistics are cited inline with source name
- [ ] The file is a single self-contained HTML (Chart.js loads from CDN)

---

## Diagram & chart guide

The template already includes Chart.js from CDN. Use `<canvas>` + an inline `<script>` block
to create charts. **Always place charts after the relevant prose**, not before.

### Chart.js setup (already in template `<head>`)

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.umd.min.js"></script>
```

### Chart types to use by section

| Section               | Recommended chart               | Chart.js type                       |
| --------------------- | ------------------------------- | ----------------------------------- |
| Market Opportunity    | TAM/SAM/SOM horizontal bars     | `bar` (horizontal, `indexAxis:'y'`) |
| Market Opportunity    | Market growth trend             | `line`                              |
| Financial Projections | Revenue Year 1/2/3 grouped bars | `bar`                               |
| Financial Projections | Investment allocation           | `doughnut`                          |
| Financial Projections | Monthly revenue ramp line       | `line`                              |
| Competitive Landscape | Feature comparison bars         | `bar` (horizontal)                  |
| Business Model        | Revenue stream breakdown        | `doughnut` or `pie`                 |
| Growth                | Projected market share growth   | `line`                              |

### TAM/SAM/SOM horizontal bar (Market section)

```html
<div class="chart-wrap" style="max-width:560px;margin:20px auto">
  <canvas id="tamChart"></canvas>
</div>
<script>
  new Chart(document.getElementById("tamChart"), {
    type: "bar",
    data: {
      labels: [
        "TAM – Total Market",
        "SAM – Addressable",
        "SOM – Obtainable (Yr 1)",
      ],
      datasets: [
        {
          label: "Market Size (M USD)", // adapt currency
          data: [450, 80, 4], // replace with real values
          backgroundColor: ["#1b6ca833", "#1b6ca866", "var(--c-primary)"],
          borderColor: ["#1b6ca8", "#1b6ca8", "var(--c-primary)"],
          borderWidth: 2,
          borderRadius: 6,
        },
      ],
    },
    options: {
      indexAxis: "y",
      responsive: true,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: (ctx) => " " + ctx.parsed.x.toLocaleString() + " M",
          },
        },
      },
      scales: {
        x: { beginAtZero: true, grid: { color: "#e2e8f0" } },
        y: { grid: { display: false } },
      },
    },
  });
</script>
```

### Revenue projection grouped bar (Financial section)

```html
<div class="chart-wrap" style="margin:20px 0">
  <canvas id="revenueChart"></canvas>
</div>
<script>
  new Chart(document.getElementById("revenueChart"), {
    type: "bar",
    data: {
      labels: ["Année 1", "Année 2", "Année 3"], // or Year 1/2/3
      datasets: [
        {
          label: "Chiffre d'affaires",
          data: [12000000, 20000000, 32000000],
          backgroundColor: "var(--c-primary)",
          borderRadius: 6,
        },
        {
          label: "Bénéfice net",
          data: [1200000, 4000000, 9000000],
          backgroundColor: "var(--c-accent)",
          borderRadius: 6,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: { legend: { position: "top" } },
      scales: {
        y: {
          beginAtZero: true,
          grid: { color: "#e2e8f0" },
          ticks: { callback: (v) => v.toLocaleString() },
        },
        x: { grid: { display: false } },
      },
    },
  });
</script>
```

### Investment donut (Financial section)

```html
<div class="chart-wrap" style="max-width:340px;margin:0 auto">
  <canvas id="investChart"></canvas>
</div>
<script>
  new Chart(document.getElementById("investChart"), {
    type: "doughnut",
    data: {
      labels: [
        "Équipement",
        "Aménagement",
        "Stock initial",
        "Frais dépôt/licences",
        "Fonds de roulement",
        "Imprévus",
      ],
      datasets: [
        {
          data: [35, 25, 20, 8, 8, 4], // percentages summing to 100
          backgroundColor: [
            "#0f4c75",
            "#1b6ca8",
            "#2980b9",
            "#e8a020",
            "#27ae60",
            "#95a5a6",
          ],
          borderWidth: 2,
          borderColor: "#fff",
          hoverOffset: 6,
        },
      ],
    },
    options: {
      responsive: true,
      cutout: "62%",
      plugins: {
        legend: { position: "right", labels: { font: { size: 12 } } },
      },
    },
  });
</script>
```

### Competitive positioning horizontal bars

```html
<div class="chart-wrap" style="margin:20px 0">
  <canvas id="compChart"></canvas>
</div>
<script>
  new Chart(document.getElementById("compChart"), {
    type: "bar",
    data: {
      labels: [
        "Prix compétitif",
        "Qualité produit",
        "Proximité",
        "Service client",
        "Digital / e-commerce",
      ],
      datasets: [
        {
          label: "[Votre projet]",
          data: [85, 90, 95, 88, 70],
          backgroundColor: "var(--c-primary)",
          borderRadius: 4,
        },
        {
          label: "Concurrent A",
          data: [70, 75, 55, 60, 80],
          backgroundColor: "#e2e8f0",
          borderRadius: 4,
        },
        {
          label: "Concurrent B",
          data: [95, 55, 40, 45, 30],
          backgroundColor: "#cbd5e1",
          borderRadius: 4,
        },
      ],
    },
    options: {
      indexAxis: "y",
      responsive: true,
      plugins: { legend: { position: "top" } },
      scales: {
        x: {
          min: 0,
          max: 100,
          grid: { color: "#e2e8f0" },
          ticks: { callback: (v) => v + "%" },
        },
        y: { grid: { display: false } },
      },
    },
  });
</script>
```

### Chart wrapper CSS (already in template)

```css
.chart-wrap {
  position: relative;
  max-width: 100%;
}
.chart-title {
  font-size: 13px;
  font-weight: 600;
  color: var(--c-text-mute);
  text-align: center;
  margin-bottom: 8px;
}
```

### Diagram placement rules

- Always give each `<canvas>` a **unique `id`** (e.g. `tamChart`, `revenueChart`, `investChart`)
- Place all `<script>` blocks **after** the `<canvas>` element, not in `<head>`
- **Replace the example data arrays** with the actual numbers you've determined from research
- Keep charts compact on screen (max-width 600px for donut/horizontal bars)
- On print/PDF: charts render as images — no special handling needed

---

## Component reference

The template provides these ready-to-use HTML components.
Use them when adding content beyond the placeholder structure.

```html
<!-- KPI box (use inside .kpi-strip grid) -->
<div class="kpi">
  <div class="kpi-val">2.4M€</div>
  <div class="kpi-label">Year 1 Revenue Target</div>
</div>

<!-- Callout box -->
<div class="box box-accent"><strong>Title</strong>Content here.</div>
<div class="box box-info"><strong>Title</strong>Content here.</div>
<div class="box box-success"><strong>Title</strong>Content here.</div>
<div class="box box-warning"><strong>Title</strong>Content here.</div>

<!-- Card grid -->
<div class="grid">
  <div class="card">
    <h3>Title</h3>
    <ul>
      <li>Point</li>
    </ul>
  </div>
</div>

<!-- Financial row -->
<div class="fin-row">
  <span>Staff salary</span><span><strong>150 000 FCFA</strong></span>
</div>
<div class="fin-row total"><span>Total</span><span>300 000 FCFA</span></div>

<!-- Timeline item -->
<li>
  <div class="tl-dot">Q1</div>
  <div class="tl-content">
    <div class="tl-period">Months 1–3</div>
    <h4>Setup &amp; Legal</h4>
    <p>Incorporate, secure location, obtain permits.</p>
  </div>
</li>

<!-- Risk table row -->
<tr>
  <td><strong>Cash flow</strong></td>
  <td>Under-capitalisation risk in first 3 months.</td>
  <td><span class="risk-high">High</span></td>
  <td>Maintain 2-month reserve. Access micro-credit line.</td>
</tr>

<!-- Badge -->
<span class="badge badge-primary">Label</span>
<span class="badge badge-accent">Label</span>

<!-- Progress bar (for market share, completion %, etc.) -->
<div class="progress-item">
  <div class="progress-label"><span>Digital channel</span><span>65%</span></div>
  <div class="progress-bar">
    <div class="progress-fill" style="width:65%"></div>
  </div>
</div>
```

---

## Resources

- `assets/template.html` — **read this first** before generating HTML. It is the structural foundation.
- `references/sections-guide.md` — detailed content guidance for every section + colour themes
- `references/user-info-guide.md` — info extraction, gap-filling benchmarks, question templates
