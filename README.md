
# TD Commercial Banking — Client & Credit Command Center

A portfolio demonstration built for a **Commercial Banking Associate** application. The app is designed to feel like an internal relationship-management and underwriting workspace for a mid-market commercial banking team.

## What the app demonstrates

The project combines the core lenses a commercial banker would use when reviewing a client relationship:

- Financial performance: revenue, EBITDA, EBITDA margin
- Credit: Debt / EBITDA, DSCR, current ratio, debt capacity
- Facility management: authorized facility, drawn exposure, utilization
- Covenant monitoring: leverage ceiling, DSCR floor, covenant headroom
- Stress testing: revenue growth/decline, margin compression, interest-rate shock, incremental draws
- Working capital: receivable days, inventory days, payable days, cash conversion cycle
- Relationship economics: lending revenue, deposits, cash-management fees, treasury opportunity
- Portfolio triage: compare multiple borrowers on leverage, coverage, deposits and risk
- Banker actions: next-best actions after reviewing the client

## Why it is relevant to Commercial Banking

Commercial banking is not only about approving a loan. The banker needs to understand the client's business, cash flows, liquidity, financial risk, industry context, borrowing needs, deposits, treasury services and overall relationship value.

This app was intentionally designed around that full relationship lens.

## Run locally

```bash
cd td_commercial_banking_command_center
python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py
```

If `streamlit` is already installed, this also works:

```bash
python3 -m streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Create a new GitHub repository.
2. Upload:
   - `app.py`
   - `requirements.txt`
   - the full `assets/` folder
3. In Streamlit Community Cloud, select the repository and choose `app.py` as the entry point.
4. Deploy.

## Suggested repository description

**Relationship-first commercial banking dashboard for mid-market credit analysis, covenant monitoring, working-capital diagnostics, stress testing and relationship economics. Built in Python + Streamlit using synthetic data.**

## Suggested project title on resume

**TD-Inspired Commercial Banking Client & Credit Command Center | Python, Streamlit, Plotly**

## Resume bullet

Built a Streamlit commercial-banking decision tool integrating financial analysis, leverage and DSCR stress testing, covenant monitoring, working-capital diagnostics, facility utilization, deposit opportunities and relationship economics across a synthetic mid-market portfolio.

## Portfolio disclaimer

Independent portfolio demonstration using synthetic data. This project is not affiliated with, endorsed by or commissioned by TD Bank Group.
