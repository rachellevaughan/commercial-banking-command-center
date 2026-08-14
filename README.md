# TD Commercial Banking | Client & Credit Command Center

### A relationship-focused credit and client analytics tool for mid-market commercial banking

The **Client & Credit Command Center** is an interactive commercial banking analytics application designed to help bankers better understand their clients and support informed lending decisions.

By bringing together financial performance, credit capacity, covenant resilience, working-capital needs, and relationship opportunities, the application provides a holistic view of a mid-market client — helping a commercial banker assess both **risk and opportunity** in one place.

> **Portfolio Project:** This is an independent project created using synthetic data for demonstration purposes. It is not affiliated with, endorsed by, or commissioned by TD Bank Group.

---

## 🔗 Explore the Project

### Live Demo
**[Launch the Interactive App →](YOUR_STREAMLIT_URL_HERE)**

Explore different client profiles, adjust credit assumptions, stress-test financial performance, and see how changes flow through to lending metrics and credit recommendations.

### Source Code
**[View the GitHub Repository →](YOUR_GITHUB_URL_HERE)**

---

## 📸 Page Preview

![Client & Credit Command Center Preview](assets/app-preview.png)

*Interactive commercial banking dashboard combining relationship analytics, credit assessment, covenant monitoring, and working-capital analysis.*

---

## Why I Built This

Commercial banking requires more than analyzing financial statements. A strong commercial banker needs to understand the **business behind the numbers** — how a client generates cash, uses credit, manages working capital, withstands downside scenarios, and could benefit from a broader banking relationship.

I built this project to explore that decision-making process through an interactive tool.

The application is designed around a simple question:

> **How can a commercial banker combine financial analysis, credit judgment, and relationship insight to make better decisions for both the client and the bank?**

Rather than presenting financial metrics in isolation, the tool connects them to practical commercial banking decisions.

---

## What the Application Does

The Command Center provides four complementary views of a commercial banking relationship:

### 1. Relationship 360

Provides a consolidated view of the client and identifies opportunities beyond the core lending relationship.

The application evaluates:

- Revenue and EBITDA performance
- Existing credit exposure
- Deposit balances
- Facility utilization
- Estimated relationship economics
- Deposit growth opportunities
- Treasury and cash management opportunities
- Suggested next actions for the commercial banker

The objective is to evaluate the client as a **relationship**, rather than simply as a loan.

---

### 2. Credit & Covenant Analysis

Evaluates the borrower's financial capacity and resilience under different operating scenarios.

Key metrics include:

- **Debt / EBITDA** — evaluates leverage relative to operating earnings
- **Debt Service Coverage Ratio (DSCR)** — assesses the borrower's ability to service debt
- **Current Ratio** — provides an indicator of short-term liquidity
- **Facility Utilization** — measures usage of available borrowing capacity
- **Covenant Headroom** — evaluates the client's flexibility relative to illustrative credit thresholds
- **Debt Capacity** — estimates additional capacity supported by the borrower's earnings profile

The application translates these metrics into a structured **Credit Memo Summary** covering:

1. Business Performance
2. Leverage
3. Debt Service Capacity
4. Liquidity & Facility Usage
5. Relationship Opportunity
6. Credit Recommendation

---

### 3. Cash Flow & Working Capital

Profitability does not always translate directly into liquidity.

This section evaluates the client's operating cash cycle through:

- Accounts receivable days
- Inventory days
- Accounts payable days
- Cash conversion cycle
- Monthly borrowing trends
- Deposit trends
- Working-capital borrowing dependence

This helps illustrate how changes in operating efficiency can affect liquidity requirements even when EBITDA remains healthy.

---

### 4. Portfolio View

Commercial bankers and credit teams often manage multiple relationships simultaneously.

The Portfolio View provides a high-level comparison of synthetic mid-market clients across:

- Revenue
- EBITDA
- Debt
- Leverage
- DSCR
- Facility utilization
- Deposits
- Cash conversion cycle
- Credit risk indicators

An interactive **Credit Risk Map** helps identify relationships that may warrant closer review based on leverage and debt service coverage.

---

## Interactive Scenario Analysis

The application allows the user to change key assumptions and immediately observe their impact on the client's credit profile.

Users can stress-test:

| Scenario Variable | Commercial Banking Purpose |
|---|---|
| Revenue Growth / Decline | Tests sensitivity to changes in business performance |
| EBITDA Margin | Evaluates the impact of operating margin expansion or compression |
| Interest-Rate Shock | Tests debt service capacity under higher borrowing costs |
| Incremental Facility Draw | Evaluates the effect of additional borrowing |
| Deposit Growth Opportunity | Identifies potential operating-balance consolidation |
| Treasury Opportunity | Illustrates potential relationship expansion |

These assumptions dynamically update leverage, DSCR, facility utilization, covenant headroom, debt capacity, and the resulting credit recommendation.

---

## Example Credit Decision Framework

Based on the selected scenario, the application categorizes the relationship into one of three illustrative outcomes:

**Proceed**  
Financial performance indicates adequate debt service capacity, manageable leverage, and sufficient liquidity.

**Proceed with Conditions**  
The relationship may remain financeable, but reduced covenant flexibility could warrant additional monitoring or structural protections.

**Escalate / Re-Structure**  
The scenario indicates material pressure on leverage or debt service capacity and may require reconsideration of exposure, structure, amortization, or other risk mitigants.

These outputs are illustrative and are intended to demonstrate analytical logic rather than represent any financial institution's actual underwriting policies.

---

## Skills Demonstrated

This project brings together skills relevant to commercial banking, financial analysis, and relationship management:

**Credit & Financial Analysis**
- Financial statement interpretation
- Leverage analysis
- Debt service capacity
- Liquidity assessment
- Covenant analysis
- Scenario and sensitivity analysis
- Working-capital analysis

**Commercial Banking**
- Mid-market client assessment
- Lending capacity
- Relationship economics
- Deposit opportunities
- Cash management opportunities
- Portfolio monitoring
- Credit recommendation development

**Analytics & Technology**
- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Interactive dashboard development
- Scenario modelling
- Data visualization

**Business Communication**
- Executive-level financial summaries
- Credit memo writing
- Translating financial metrics into business implications
- Data storytelling
- Decision-oriented recommendations

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Financial calculations and application logic |
| **Streamlit** | Interactive web application |
| **Pandas** | Data transformation and portfolio analysis |
| **NumPy** | Scenario calculations |
| **Plotly** | Interactive financial visualizations |

---

## Project Structure

```text
td-commercial-banking-command-center/
│
├── app.py
├── requirements.txt
├── README.md
│
└── assets/
    ├── TD-logo.png
    ├── TD-toronto.jpeg
    ├── Td-commercial.png
    └── app-preview.png
```

---

## Run Locally

Clone the repository:

```bash
git clone YOUR_GITHUB_URL_HERE
```

Navigate to the project:

```bash
cd td-commercial-banking-command-center
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
streamlit run app.py
```

---

## Data & Methodology

All companies, financial information, credit scenarios, thresholds, relationship economics, and recommendations used in this application are **synthetic and illustrative**.

No confidential, proprietary, client, or internal TD information was used in the development of this project.

The financial logic is intentionally simplified to demonstrate commercial banking concepts in an interactive portfolio environment and should not be interpreted as actual underwriting methodology or financial advice.

---

## About This Project

This project was developed as part of my broader portfolio at the intersection of **finance, analytics, strategy, and technology**.

I am particularly interested in how analytics can help financial professionals move beyond reporting — bringing together quantitative analysis and business judgment to better understand clients, evaluate risk, identify opportunities, and support stronger decisions.

---
*Independent portfolio demonstration using synthetic data. This project is not affiliated with, endorsed by, or commissioned by TD Bank Group.*
