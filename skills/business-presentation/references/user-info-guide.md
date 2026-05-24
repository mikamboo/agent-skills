# User Information Extraction Guide

This file describes how to extract key business information from the user's idea
description, what questions to ask if critical data is missing, and how to fill
gaps with reasonable estimates.

---

## Step 1 — Parse the idea description

From the raw text the user provides, extract as many of these fields as possible:

| Field                 | Look for                                                            |
| --------------------- | ------------------------------------------------------------------- |
| `company_name`        | Any existing brand/company name mentioned                           |
| `project_name`        | The project or product name                                         |
| `sector`              | Food, retail, tech, health, agri, services, education, logistics…   |
| `geography`           | Country, city, region, neighbourhood                                |
| `target_customer`     | Who buys: individuals, SMEs, B2B, age group, income level           |
| `core_offering`       | What is sold or provided                                            |
| `business_model`      | How money is made (product sales, subscriptions, commissions, B2B…) |
| `initial_investment`  | Any budget or funding mentioned                                     |
| `currency`            | FCFA, USD, EUR, GBP, XAF, NGN, KES, MAD, etc.                       |
| `language`            | Language of the description → use same language for output          |
| `team_info`           | Names, roles, experience mentioned                                  |
| `competitive_context` | Any competitors mentioned                                           |
| `unique_advantage`    | Any USP, proprietary element, or exclusive partner mentioned        |
| `timeline_target`     | Any launch date or milestones mentioned                             |
| `growth_ambition`     | Scale-up, franchise, exit, lifestyle business?                      |

---

## Step 2 — Determine what is CRITICAL vs INFERABLE

### Always knowable from context (do NOT ask):

- Sector — can be inferred from the product/service described
- Target customer — can be inferred from sector and product
- Competitive landscape — use knowledge of the sector
- SWOT — can be derived from sector + geography
- Risk analysis — standard per sector
- Colour theme — pick based on sector
- Language — match the user's input language

### Items to estimate if missing (mark as **(est.)**):

- Market size — use common benchmarks for the sector/region
- Revenue projection — use conservative sector averages
- Investment estimate — use typical startup costs for the sector/scale
- Margins — use standard sector margins

### Only ask the user if truly critical AND un-inferable:

Priority questions — ask at most 2–3, only what really changes the document:

1. **Company/founder name** — needed for the header. If not provided, ask.
2. **Location specifics** — city or neighbourhood matters for market analysis. If vague, ask.
3. **Investment budget** — if the user hasn't mentioned any number, this shapes the financial section. Ask if discussing a capital raise.

Do NOT ask about:

- Sector (inferable)
- Competitors (you know them)
- Market size (you can research/estimate)
- SWOT bullets (you can generate these)
- Risk table (standard per sector)

---

## Step 3 — "Fill the gaps" heuristics by sector

Use these benchmarks when specific numbers are absent.
Always mark estimates with **(est.)** in the output.

### Retail / Proximity Commerce (small shop, boutique, épicerie)

- Initial investment: **3–10M FCFA** / **5k–20k USD** for a small unit
- Gross margin: **15–25%**
- Monthly operating cost: **10–20% of revenue**
- Breakeven: **3–6 months**
- Daily sales estimate: start with 50–150 customers × average basket

### Food & Beverage (restaurant, catering, snack bar)

- Initial investment: **5–25M FCFA** / **10k–50k USD**
- Gross margin: **60–70%** (food cost ~30–35%)
- Monthly operating cost: heavy (staff + rent + food waste)
- Breakeven: **6–12 months**

### Agriculture / Agri-processing

- Project timelines are seasonal → use crop cycles
- Initial investment highly variable (land, equipment, storage)
- Margin depends hugely on value-added processing vs raw commodity

### Digital / SaaS / App

- Initial investment: **development cost** + 3–6 months of runway
- Gross margin: **70–90%** (software)
- Customer acquisition cost (CAC) is the key metric
- Breakeven: 12–24 months typical

### Services / Consulting / Training

- Low capital intensity
- Revenue = # clients × rate × hours
- Key cost: founder/staff time, marketing
- Breakeven: 1–3 months

### Logistics / Transport / Delivery

- Initial investment dominated by vehicles / fleet
- Gross margin: **20–40%**
- Key variable: fuel + maintenance

### Health / Clinic / Pharmacy

- Regulatory complexity — mention permitting in roadmap
- Initial investment: equipment + fit-out intensive
- Revenue per patient / per prescription

---

## Step 4 — How to ask questions (if needed)

When you must ask questions, be concise and friendly. Ask all missing critical
questions in ONE turn, not one at a time. Frame them as "quick questions to
personalise your presentation" — not a questionnaire.

**Example phrasing (adapt language to match user):**

> Before I generate the full presentation, just 2 quick things to personalise it:
>
> 1. What is the name of the company or founder behind this project?
> 2. Do you have an approximate budget in mind for the launch?

Never ask more than 3 questions. If the user doesn't answer, use defaults
(e.g. "Founder" as company name, a typical investment range for the sector).

---

## Step 5 — Output format decision

The user asked for **HTML or PDF**:

- **Default output**: a single self-contained `.html` file (can be opened in browser and printed to PDF)
- **If user says PDF only**: generate the HTML and add a note explaining how to print to PDF (Ctrl+P → Save as PDF)
- **File name format**: `[CompanyName]-[ProjectName]-presentation.html` (lowercase, hyphens)

---

## Step 6 — Post-generation quality check

Before finalising the HTML file, verify:

- [ ] All `__PLACEHOLDER__` tokens have been replaced
- [ ] Chart data placeholders (`__TAM_VALUE__`, `__REV_Y1__`, `__INVEST_LABELS__`, etc.) fully replaced
- [ ] Chart values in JavaScript match numbers stated in the prose and tables
- [ ] Each `<canvas>` element has a unique ID and a matching `new Chart(...)` call in the script block
- [ ] The nav links match the actual section IDs
- [ ] The section numbers are sequential (re-number if sections were added/removed)
- [ ] Currency is consistent throughout
- [ ] Language is consistent throughout
- [ ] The `.kpi-strip` has real values (not placeholders)
- [ ] The SWOT has real content in all 4 quadrants
- [ ] Risk table has ≥ 5 risks with concrete mitigations
- [ ] Financial section has real numbers (even if estimated)
- [ ] Web-sourced statistics are cited with source name inline
- [ ] The footer tagline is meaningful
