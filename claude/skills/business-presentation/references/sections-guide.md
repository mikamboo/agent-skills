# Section Content Guidelines

This file describes what to write in each section of a business presentation.
Reference it when generating content. Adapt depth and detail to what is known.

---

## 1. Executive Summary

**Goal:** A busy investor/partner should grasp the entire project in 90 seconds.

Include:

- 4 KPI boxes: pick the 4 most impactful numbers (investment needed, monthly revenue target, ROI timeline, market size, or key unit economics)
- 2–3 paragraph summary covering: what the business does, for whom, why now, and why it will succeed
- A crisp "Key Value Proposition" callout — one sentence that explains the unique advantage

**Do not** repeat every detail — summarise and intrigue.

---

## 2. Company & Vision

Include:

- What the founding entity is (existing company, new venture, solo entrepreneur)
- Mission statement or core purpose (why this exists beyond profit)
- Short-term goal (12–18 months) and long-term vision (3–5 years)
- Key objectives as a short bullet list (3–5 items)

If no company exists yet, describe the intended legal form.

---

## 3. Market Opportunity

Include:

- Market definition: what sector, what geography, what customer segment
- Market size data (TAM/SAM/SOM if possible, or at least directional estimates) — **sourced from web research**
- Key market trends or structural factors driving demand — **cite the source**
- 3–4 stat boxes if you have compelling numbers (use `.kpi-strip` or `.stat-box` equivalents)
- Context on why this is the right moment (regulatory, demographic, technological)

Use grid cards to highlight 3–5 structural factors or growth drivers.

**Diagram required:** TAM/SAM/SOM horizontal bar chart (`tamChart`).
Set realistic values from your web research. If true TAM is unknown, use the closest
available proxy (e.g. national retail sector size, e-commerce market) and label clearly.
Optional addition: add a `line` chart showing the market's growth rate over 3–5 years
if CAGR data is found.

---

## 4. Product / Service

Include:

- Clear description of what is offered (products, services, or both)
- Categorise into 2–4 groups if there are multiple offerings
- Use a grid of cards — one card per category, with a sub-list of items
- Highlight any proprietary, exclusive, or differentiated products
- Mention pricing approach if known

---

## 5. Business Model

Include:

- Revenue streams: how and from whom does money come in
- Unit economics if available (cost per unit, price per unit, margin)
- Operating model: who does what (staff structure, outsourced vs in-house)
- Key operational assumptions (opening hours, inventory turns, capacity)
- Customer acquisition approach

---

## 6. Competitive Landscape

Include:

- Direct competitors (name them if known, or characterise them: "informal street vendors", "large supermarkets")
- Indirect competitors / substitutes
- Competitive positioning: where does this business sit on price vs quality vs convenience axes
- Key differentiators (use a box-info or boxes)
- Barriers to entry this project will build over time

**Diagram required:** Competitive positioning horizontal bar chart (`compChart`).

- Name 2–4 actual competitors found in your web research as dataset labels
- Choose 4–6 comparison criteria relevant to the sector (e.g. price, proximity, quality, digital, range)
- Score each competitor and this project on each criterion (0–100 scale, your judgement)
- This chart makes the positioning immediately visual and compelling to investors

---

## 7. SWOT Analysis

Fill all four quadrants with 4–6 bullet points each.

- **Strengths**: internal advantages that exist today
- **Weaknesses**: internal limitations or gaps
- **Opportunities**: external trends or gaps the business can exploit
- **Threats**: external risks (competitive, regulatory, economic, social)

Be honest — shallow SWOT analysis loses credibility with investors.

---

## 8. Go-To-Market Strategy

Include:

- Target customer profile (who is the ideal first customer; describe in 2–3 sentences)
- Channel strategy: how do customers find the business and how do they buy
- Launch plan: what happens in the first 30/60/90 days to attract first customers
- Retention strategy: how to keep customers coming back
- Marketing / communication approach (social, word of mouth, local presence, etc.)

Use callout boxes to highlight key strategies.

---

## 9. Implementation Roadmap

Structure as a timeline with 3–5 phases.
Standard phases for most projects:

- **Phase 1 (Months 1–2):** Setup & Legal — incorporation, location, permits, suppliers
- **Phase 2 (Months 2–3):** Build & Fit-out — renovation, equipment, stock procurement
- **Phase 3 (Month 3–4):** Soft Launch — test operations, staff training, initial customers
- **Phase 4 (Month 4+):** Full Operations — marketing push, optimise, scale
- **Phase 5 (Year 2+):** Growth — expansion, new offerings, partnerships

Adapt phase names and durations to the specific project.
Use the `.timeline` list component.

---

## 10. Financial Projections

**Always include these sub-sections:**

### Initial Investment Table

List every cost bucket needed to open/launch:

- Capital expenditure (equipment, fit-out, vehicles, IP, tech)
- Working capital / initial stock
- Security deposits, licenses, registration fees
- Contingency (5–10%)

### Revenue Forecast

Show at minimum:

- Daily/weekly revenue assumption
- Monthly revenue (gross)
- Gross margin % assumption
- Gross profit monthly
- Net profit estimate after opex

If multi-year, show Year 1 / Year 2 / Year 3 targets.

### Monthly Operating Costs (OPEX) Table

List all recurring costs: salaries, rent, utilities, marketing, logistics, maintenance, etc.

### Financial Summary Box (box-success)

State: monthly breakeven revenue, expected monthly net profit, payback period on initial investment.

**Currency note:** Use the currency relevant to the context. If the user mentions FCFA, USD, EUR, etc., use that throughout.

**Diagrams required:**

1. **Revenue projection bar chart** (`revenueChart`) — grouped bars for each year showing gross revenue
   and net profit side by side. Values must match the table above exactly.
2. **Investment allocation donut** (`investChart`) — shows % of total investment per cost category.
   Use the category labels from the investment table. Express as percentages summing to 100.

**Optional addition:** Add a monthly revenue ramp-up `line` chart (months 1–12) showing the
path to breakeven. This is very compelling for investors when the breakeven is >3 months away.

---

## 11. Risk Analysis

Use the risk table. Include 6–10 risks covering:

- Operational risks (staff, supply chain, equipment)
- Financial risks (cash flow, under-capitalisation)
- Market risks (competition, demand change)
- Regulatory / legal risks
- External risks (security, weather, macro-economic)

Risk levels:

- `<span class="risk-high">High</span>` — could kill the business
- `<span class="risk-med">Medium</span>` — significant but manageable
- `<span class="risk-low">Low</span>` — minor, easy to mitigate

Each risk must have a concrete mitigation strategy — not just "monitor the situation."

---

## 12. Growth & Scalability

Include:

- Medium-term growth levers (new products, new locations, new customer segments)
- Long-term vision for scale (franchise model, platform, regional expansion)
- Technology or digitalisation opportunities
- Partnership or integration opportunities
- Use a grid of 4–6 cards, one per growth vector

---

## 13. Key Success Factors

Include 4–6 critical factors that will determine whether this business succeeds or fails.
These are the things the team must execute perfectly. Each factor should:

- Have a clear label
- Have 2–3 sentences explaining why it is critical
- Be concrete, not generic ("hire a great team" is generic; "retain a store manager with 3+ years retail experience" is concrete)

Use `.card` grid layout.

---

## 14. Team (include only if team info is available)

For each key person:

- Name and role
- Relevant background (2–3 sentences)
- Key contribution to this project

If no team info is provided, omit this section or replace with "Team to be recruited" with a brief staffing plan.

---

## 15. Conclusion & Next Steps

Include:

- Restate the opportunity in 1–2 sentences
- State the ask (if fundraising: how much, for what)
- List 5–7 immediate concrete actions numbered sequentially (box-info)
- Closing statement on confidence / timing

---

## Colour Theme Selection Guide

Choose the theme that best matches the business sector / brand personality:

| Theme name       | Primary colour | Best for                                     |
| ---------------- | -------------- | -------------------------------------------- |
| `teal` (default) | `#0f4c75`      | Finance, professional services, B2B          |
| `green`          | `#1f7a4c`      | Agriculture, food, environment, local retail |
| `indigo`         | `#3949ab`      | Tech, SaaS, digital services                 |
| `amber`          | `#b45309`      | Engineering, logistics, construction         |
| `rose`           | `#9d174d`      | Beauty, fashion, hospitality                 |
| `slate`          | `#334155`      | Consulting, legal, government                |

To apply a theme, override the `:root` CSS variables in the `<style>` block:

- `--c-primary` = darkest shade
- `--c-primary-mid` = mid shade
- `--c-primary-light` = very light background tint (5–8% saturation)

**Green theme example (à la K-BOUTIQUE):**

```css
--c-primary: #1f7a4c;
--c-primary-mid: #27ae60;
--c-primary-light: #e8f5ee;
--c-accent: #e6a817;
```

---

## Language & Tone

- Match the language of the user's idea description (French → French output, English → English output, etc.)
- Tone: professional but accessible — avoid heavy jargon unless the sector demands it
- Numbers: format consistently (thousands separator, currency symbol placement)
- Dates: use the convention of the target country
- When specific numbers are not known, use realistic estimates and mark them with **(est.)** or **(hypothèse)**
