from pathlib import Path
import textwrap

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Commercial Banking | Client & Credit Command Center",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# FILE PATHS
# ============================================================

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

TD_LOGO = ASSETS / "TD-logo.png"
TD_TORONTO = ASSETS / "TD-toronto.jpeg"
TD_COMMERCIAL = ASSETS / "Td-commercial.png"


# ============================================================
# COLOURS
# ============================================================

TD_GREEN = "#008A00"
TD_DARK = "#0B3B2E"
TD_FOREST = "#14543D"
TD_MID = "#37765A"
TD_LIGHT = "#EAF4EC"

INK = "#17251F"
BODY = "#35473E"
MUTED = "#697970"
BORDER = "#D7E3DA"
BORDER_SOFT = "#E6EDE8"

AMBER = "#A86A10"
RED = "#B42318"
WHITE = "#FFFFFF"


# ============================================================
# HTML HELPER
# ============================================================

def render_html(content):
    st.html(textwrap.dedent(content).strip())


# ============================================================
# GLOBAL CSS
# ============================================================

render_html(
    f"""
    <style>

    .stApp {{
        background: linear-gradient(
            180deg,
            #F8FBF9 0%,
            #FFFFFF 38%,
            #F7FAF8 100%
        );
        color: {INK};
    }}

    .block-container {{
        max-width: 1450px;
        padding-top: 1.8rem;
        padding-left: 2.4rem;
        padding-right: 2.4rem;
        padding-bottom: 3rem;
    }}

    .stMarkdown p {{
        font-size: 18px !important;
        line-height: 1.6 !important;
        color: {BODY} !important;
    }}

    [data-testid="stCaptionContainer"] {{
        font-size: 15px !important;
        line-height: 1.5 !important;
        color: {MUTED} !important;
    }}

    h1 {{
        font-size: 44px !important;
        line-height: 1.08 !important;
        color: {TD_DARK} !important;
        font-weight: 800 !important;
    }}

    h2 {{
        font-size: 32px !important;
        line-height: 1.15 !important;
        color: {TD_DARK} !important;
        font-weight: 800 !important;
    }}

    h3 {{
        font-size: 23px !important;
        line-height: 1.25 !important;
        color: {TD_DARK} !important;
        font-weight: 800 !important;
    }}

    [data-testid="stSidebar"] {{
        background: #F6F9F7;
        border-right: 1px solid {BORDER};
    }}

    [data-testid="stSidebar"] h3 {{
        font-size: 20px !important;
        font-weight: 800 !important;
    }}

    [data-testid="stSidebar"] p {{
        font-size: 16px !important;
    }}

    [data-testid="stSidebar"] label p,
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {{
        font-size: 16px !important;
        font-weight: 650 !important;
    }}

    [data-testid="stSidebar"] [data-baseweb="select"],
    [data-testid="stSidebar"] [data-baseweb="select"] * {{
        font-size: 16px !important;
    }}

    .eyebrow {{
        color: {TD_GREEN};
        font-size: 14px;
        font-weight: 850;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }}

    .hero-title {{
        color: {TD_DARK};
        font-size: 46px;
        line-height: 1.07;
        font-weight: 850;
        letter-spacing: -0.035em;
        margin-bottom: 14px;
    }}

    .hero-sub {{
        color: #56685F;
        font-size: 18px;
        line-height: 1.65;
        max-width: 850px;
    }}

    .status-pill {{
        display: inline-block;
        padding: 8px 12px;
        border-radius: 999px;
        background: {TD_LIGHT};
        border: 1px solid #CFE4D4;
        color: {TD_DARK};
        font-size: 14px;
        font-weight: 750;
        margin-right: 6px;
        margin-top: 14px;
    }}

    .client-name {{
        color: {TD_DARK};
        font-size: 34px;
        font-weight: 850;
        line-height: 1.15;
        letter-spacing: -0.025em;
    }}

    .client-sub {{
        color: {MUTED};
        font-size: 16px;
        line-height: 1.5;
        margin-top: 6px;
        margin-bottom: 18px;
    }}

    .metric-card {{
        background: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 16px;
        padding: 20px 18px;
        min-height: 155px;
        box-shadow: 0 5px 18px rgba(21,58,40,0.05);
    }}

    .metric-label {{
        color: #65756D;
        font-size: 14px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }}

    .metric-value {{
        color: {TD_DARK};
        font-size: 30px;
        font-weight: 850;
        line-height: 1.05;
        margin-top: 8px;
    }}

    .metric-note {{
        color: {MUTED};
        font-size: 14px;
        line-height: 1.45;
        margin-top: 10px;
    }}

    .section-card {{
        background: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 17px;
        padding: 22px 24px;
        box-shadow: 0 4px 16px rgba(14,50,34,0.04);
    }}

    .section-title {{
        color: {TD_DARK};
        font-size: 20px;
        font-weight: 850;
        line-height: 1.3;
    }}

    .section-sub {{
        color: {MUTED};
        font-size: 15px;
        line-height: 1.5;
        margin-top: 5px;
        margin-bottom: 12px;
    }}

    .mini-label {{
        color: {MUTED};
        font-size: 13px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.075em;
    }}

    .mini-value {{
        color: {TD_DARK};
        font-size: 21px;
        font-weight: 850;
        margin-top: 4px;
    }}

    .memo-section {{
        border-top: 1px solid {BORDER_SOFT};
        padding: 15px 0;
    }}

    .memo-heading {{
        color: {TD_DARK};
        font-size: 17px;
        font-weight: 850;
        margin-bottom: 5px;
    }}

    .memo-copy {{
        color: {BODY};
        font-size: 16px;
        line-height: 1.6;
    }}

    .memo-rec {{
        margin-top: 15px;
        padding: 16px 18px;
        background: #F0F7F1;
        border-left: 5px solid {TD_GREEN};
        border-radius: 10px;
    }}

    .memo-rec-label {{
        color: {MUTED};
        font-size: 13px;
        font-weight: 850;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }}

    .memo-rec-title {{
        color: {TD_DARK};
        font-size: 21px;
        font-weight: 850;
        margin-top: 4px;
    }}

    .memo-rec-copy {{
        color: {BODY};
        font-size: 16px;
        line-height: 1.55;
        margin-top: 5px;
    }}

    .decision-banner {{
        background: linear-gradient(100deg,#EAF6EC,#F8FCF9);
        border: 1px solid #CBE5D0;
        border-radius: 17px;
        padding: 20px 22px;
    }}

    .decision-title {{
        color: {TD_DARK};
        font-size: 24px;
        font-weight: 850;
        margin-top: 5px;
    }}

    .decision-copy {{
        color: #40544A;
        font-size: 16px;
        line-height: 1.6;
        margin-top: 6px;
    }}

    .risk-low {{
        color: {TD_GREEN};
    }}

    .risk-watch {{
        color: {AMBER};
    }}

    .risk-high {{
        color: {RED};
    }}

    .client-card {{
        background: #FBFDFB;
        border: 1px solid {BORDER};
        border-radius: 14px;
        padding: 14px 16px;
        margin-bottom: 10px;
    }}

    div[data-testid="stTabs"] button {{
        font-size: 16px !important;
        font-weight: 750 !important;
        color: #52635A !important;
        padding: 12px 15px !important;
    }}

    div[data-testid="stTabs"] button[aria-selected="true"] {{
        color: {TD_GREEN} !important;
    }}

    [data-testid="stDataFrame"] {{
        font-size: 15px !important;
    }}

    .stDownloadButton > button {{
        min-height: 48px !important;
        border-radius: 10px !important;
        background: {TD_GREEN} !important;
        color: white !important;
        border: none !important;
        font-size: 16px !important;
        font-weight: 750 !important;
    }}

    .stButton > button {{
        min-height: 48px !important;
        font-size: 16px !important;
        font-weight: 750 !important;
    }}

    .footer-note {{
        color: {MUTED};
        font-size: 14px;
        line-height: 1.55;
    }}

    </style>
    """
)


# ============================================================
# HELPERS
# ============================================================

def money(value, digits=0):
    value = float(value)

    if abs(value) >= 1_000_000_000:
        return f"${value / 1_000_000_000:,.{digits}f}B"

    if abs(value) >= 1_000_000:
        return f"${value / 1_000_000:,.{digits}f}M"

    if abs(value) >= 1_000:
        return f"${value / 1_000:,.{digits}f}K"

    return f"${value:,.0f}"


def pct(value, digits=1):
    return f"{float(value) * 100:.{digits}f}%"


def ratio(value, digits=2):
    return f"{float(value):.{digits}f}x"


def metric_card(label, value, note):
    render_html(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """
    )


def clean_plot(fig, height=310, showlegend=False):
    fig.update_layout(
        height=height,
        margin=dict(l=8, r=8, t=34, b=12),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Arial", color=INK, size=13),
        showlegend=showlegend,
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        tickfont=dict(size=12),
    )

    fig.update_yaxes(
        gridcolor="#E9EFEA",
        zeroline=False,
        tickfont=dict(size=12),
    )

    return fig


# ============================================================
# SYNTHETIC CLIENT DATA
# ============================================================

clients = pd.DataFrame(
    [
        [
            "Northline Industrial Supply",
            "Industrial Distribution",
            42.5,
            6.4,
            11.8,
            18.5,
            2.89,
            1.56,
            0.47,
            1.68,
            2.2,
            67,
            5.4,
            "Low",
        ],
        [
            "MaplePeak Foods",
            "Food Manufacturing",
            31.8,
            4.1,
            8.5,
            13.2,
            3.22,
            1.31,
            0.59,
            1.41,
            1.3,
            74,
            3.1,
            "Watch",
        ],
        [
            "CedarWorks Packaging",
            "Packaging",
            57.6,
            10.2,
            16.0,
            23.4,
            2.29,
            1.82,
            0.39,
            1.91,
            3.6,
            61,
            7.2,
            "Low",
        ],
        [
            "HarbourTech Services",
            "Business Services",
            24.2,
            5.7,
            6.2,
            8.0,
            1.40,
            2.14,
            0.24,
            2.32,
            4.8,
            52,
            8.6,
            "Low",
        ],
        [
            "Evergreen BuildCo",
            "Construction",
            48.9,
            5.1,
            14.4,
            19.3,
            3.78,
            1.17,
            0.63,
            1.28,
            0.9,
            82,
            2.6,
            "Watch",
        ],
    ],
    columns=[
        "Client",
        "Industry",
        "Revenue",
        "EBITDA",
        "Debt",
        "Facility",
        "Debt/EBITDA",
        "DSCR",
        "Facility Utilization",
        "Current Ratio",
        "Deposit Balance",
        "CCC Days",
        "Cash Mgmt Fees",
        "Risk",
    ],
)

for col in [
    "Revenue",
    "EBITDA",
    "Debt",
    "Facility",
    "Deposit Balance",
    "Cash Mgmt Fees",
]:
    clients[col] = clients[col] * 1_000_000


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    if TD_LOGO.exists():
        st.image(str(TD_LOGO), width=64)

    st.markdown("### Commercial Banking")
    st.caption("Client & Credit Command Center")

    selected_client = st.selectbox(
        "Select client",
        clients["Client"].tolist(),
        index=0,
        help=(
            "Select a synthetic mid-market borrower to review its "
            "credit profile and relationship opportunities."
        ),
    )

    row = clients.loc[
        clients["Client"] == selected_client
    ].iloc[0]

    st.markdown("---")
    st.markdown("#### Credit scenario")

    growth = (
        st.slider(
            "Revenue growth / (decline)",
            min_value=-20,
            max_value=20,
            value=4,
            step=1,
            help=(
                "Scenario assumption applied to current annual revenue. "
                "Negative values represent downside stress; positive values "
                "represent growth."
            ),
        )
        / 100
    )

    ebitda_margin_change = (
        st.slider(
            "EBITDA margin change (pp)",
            min_value=-8,
            max_value=8,
            value=-1,
            step=1,
            help=(
                "Change in EBITDA margin in percentage points. "
                "For example, -3 pp changes a 15% margin to 12%."
            ),
        )
        / 100
    )

    rate_shock = (
        st.slider(
            "Interest rate shock (bps)",
            min_value=0.0,
            max_value=5.0,
            value=1.0,
            step=0.25,
            help=(
                "Increase in assumed borrowing costs. "
                "For example, +2.0% represents a 200 bps shock."
            ),
        )
        / 100
    )

    incremental_draw = (
        st.slider(
            "Incremental facility draw ($M)",
            min_value=0,
            max_value=6,
            value=1,
            step=1,
            help=(
                "Additional borrowing under the client's existing "
                "commercial credit facility."
            ),
        )
        * 1_000_000
    )

    st.markdown("---")
    st.markdown("#### Relationship lens")

    deposit_growth = (
        st.slider(
            "Deposit growth opportunity",
            min_value=0,
            max_value=50,
            value=15,
            step=5,
            help=(
                "Illustrative opportunity to consolidate more of the "
                "client's operating balances and deposits."
            ),
        )
        / 100
    )

    treasury_cross_sell = st.toggle(
        "Add treasury opportunity",
        value=True,
        help=(
            "Models an illustrative treasury, payments or liquidity "
            "management opportunity."
        ),
    )

    st.markdown("---")
    st.caption(
        "All companies, metrics and scenarios are synthetic and created "
        "solely for portfolio demonstration."
    )


# ============================================================
# BASE VALUES
# ============================================================

revenue = float(row["Revenue"])
ebitda = float(row["EBITDA"])
debt = float(row["Debt"])
facility = float(row["Facility"])
utilization = float(row["Facility Utilization"])
deposits = float(row["Deposit Balance"])
cash_fees = float(row["Cash Mgmt Fees"])
ccc = float(row["CCC Days"])
current_ratio = float(row["Current Ratio"])

base_margin = ebitda / revenue


# ============================================================
# SCENARIO ENGINE
# ============================================================

stress_revenue = revenue * (1 + growth)
stress_margin = max(0.02, base_margin + ebitda_margin_change)
stress_ebitda = stress_revenue * stress_margin

base_drawn = facility * utilization
stress_drawn = min(facility, base_drawn + incremental_draw)
stress_debt = debt + incremental_draw

base_interest_rate = 0.0625
amortization_rate = 0.08

stress_debt_service = (
    stress_debt * (base_interest_rate + rate_shock)
    + stress_debt * amortization_rate
)

stress_dscr = (
    stress_ebitda / stress_debt_service
    if stress_debt_service > 0
    else 99
)

stress_leverage = (
    stress_debt / stress_ebitda
    if stress_ebitda > 0
    else 99
)

facility_utilization = (
    stress_drawn / facility
    if facility > 0
    else 0
)

covenant_limit = 3.75
dscr_floor = 1.20
current_ratio_floor = 1.25

leverage_headroom = covenant_limit - stress_leverage
dscr_headroom = stress_dscr - dscr_floor

max_debt_at_leverage = stress_ebitda * covenant_limit
debt_capacity_headroom = max(
    0,
    max_debt_at_leverage - stress_debt,
)

undrawn_availability = max(
    0,
    facility - stress_drawn,
)


# ============================================================
# RELATIONSHIP ECONOMICS
# ============================================================

deposit_opportunity = deposits * deposit_growth

treasury_fee_opportunity = (
    120_000
    if treasury_cross_sell
    else 0
)

illustrative_loan_revenue = stress_drawn * 0.032
illustrative_deposit_value = deposits * 0.009

relationship_revenue_est = (
    illustrative_loan_revenue
    + illustrative_deposit_value
    + cash_fees
    + treasury_fee_opportunity
)


# ============================================================
# CREDIT RECOMMENDATION
# ============================================================

if (
    stress_dscr >= 1.35
    and stress_leverage <= 3.25
    and current_ratio >= 1.35
):
    recommendation = "Proceed"
    rec_class = "risk-low"
    rec_text = (
        "The selected scenario indicates adequate debt service capacity, "
        "manageable leverage and sufficient liquidity. Maintain routine "
        "financial monitoring while pursuing appropriate deposit and "
        "cash management opportunities."
    )

elif (
    stress_dscr >= 1.15
    and stress_leverage <= 4.00
):
    recommendation = "Proceed with Conditions"
    rec_class = "risk-watch"
    rec_text = (
        "The relationship remains potentially financeable; however, "
        "the selected scenario reduces covenant flexibility. Consider "
        "enhanced reporting, disciplined pricing, limits on incremental "
        "leverage and closer monitoring of operating performance."
    )

else:
    recommendation = "Escalate / Re-Structure"
    rec_class = "risk-high"
    rec_text = (
        "The selected scenario materially weakens debt service capacity "
        "or leverage. Reassess requested exposure, structure, amortization, "
        "collateral support and risk-mitigation options before proceeding."
    )


# ============================================================
# HERO
# ============================================================

hero_left, hero_right = st.columns(
    [1.55, 0.95],
    gap="large",
)

with hero_left:
    render_html(
        """
        <div class="eyebrow">Commercial Banking · Toronto</div>
        <div class="hero-title">Client & Credit Command Center</div>
        <div class="hero-sub">
            A relationship focused workspace designed to support thoughtful 
            credit decisions and stronger client outcommes. It brings together
            financial performance, lending capacity, covenant resilience, working
            capital needs, and relationship opportunities to provide a clear, holistic
            view of each mid-market client.
        </div>
        <span class="status-pill">Credit underwriting</span>
        <span class="status-pill">Relationship management</span>
        <span class="status-pill">Risk monitoring</span>
        <span class="status-pill">Cash management</span>
        """
    )

with hero_right:
    if TD_TORONTO.exists():
        st.image(
            str(TD_TORONTO),
            use_container_width=True,
        )

st.markdown("")


# ============================================================
# CLIENT HEADER
# ============================================================

render_html(
    f"""
    <div class="client-name">{selected_client}</div>
    <div class="client-sub">
        {row["Industry"]}
        &nbsp;·&nbsp;
        Mid-market commercial relationship
        &nbsp;·&nbsp;
        Synthetic portfolio case
    </div>
    """
)


# ============================================================
# KPI ROW
# ============================================================

m1, m2, m3, m4, m5, m6 = st.columns(6)

direction_text = (
    "scenario growth"
    if growth >= 0
    else "scenario decline"
)

with m1:
    metric_card(
        "Revenue",
        money(revenue, 1),
        f"{pct(growth)} {direction_text}",
    )

with m2:
    metric_card(
        "EBITDA",
        money(ebitda, 1),
        f"{pct(base_margin)} current margin",
    )

with m3:
    metric_card(
        "Debt / EBITDA",
        ratio(row["Debt/EBITDA"]),
        f"{ratio(stress_leverage)} stressed",
    )

with m4:
    metric_card(
        "DSCR",
        ratio(row["DSCR"]),
        f"{ratio(stress_dscr)} stressed",
    )

with m5:
    metric_card(
        "Facility Utilization",
        pct(utilization, 0),
        f"{pct(facility_utilization, 0)} stressed",
    )

with m6:
    metric_card(
        "Deposits",
        money(deposits, 1),
        f"+{money(deposit_opportunity, 1)} potential",
    )

st.markdown("")


# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Relationship 360",
        "Credit & Covenant",
        "Cash Flow & Working Capital",
        "Portfolio View",
    ]
)


# ============================================================
# TAB 1
# ============================================================

with tab1:

    st.markdown("")

    left, right = st.columns(
        [1.35, 1],
        gap="large",
    )

    with left:

        render_html(
            f"""
            <div class="decision-banner">
                <div class="mini-label">Scenario recommendation</div>
                <div class="decision-title {rec_class}">
                    {recommendation}
                </div>
                <div class="decision-copy">
                    {rec_text}
                </div>
            </div>
            """
        )

        st.markdown("")

        render_html(
            """
            <div class="section-card">
                <div class="section-title">Relationship Economics</div>
                <div class="section-sub">
                    Illustrative annualized contribution across credit,
                    deposits and treasury services.
                </div>
            </div>
            """
        )

        economics = pd.DataFrame(
            {
                "Source": [
                    "Loan spread revenue",
                    "Deposit value",
                    "Cash management",
                    "Treasury opportunity",
                ],
                "Value": [
                    illustrative_loan_revenue,
                    illustrative_deposit_value,
                    cash_fees,
                    treasury_fee_opportunity,
                ],
            }
        )

        fig = go.Figure(
            go.Bar(
                x=economics["Value"],
                y=economics["Source"],
                orientation="h",
                marker_color=[
                    TD_GREEN,
                    TD_FOREST,
                    "#5D7F69",
                    "#9BB5A1",
                ],
            )
        )

        fig.update_traces(
            hovertemplate="%{y}<br>$%{x:,.0f}<extra></extra>"
        )

        fig.update_xaxes(
            tickprefix="$",
            tickformat=",.0f",
        )

        st.plotly_chart(
            clean_plot(
                fig,
                height=300,
            ),
            use_container_width=True,
        )

    with right:

        render_html(
            """
            <div class="section-card">
                <div class="section-title">Client Opportunity Map</div>
                <div class="section-sub">
                    Potential opportunities to deepen the relationship
                    beyond the core lending product.
                </div>
            </div>
            """
        )

        opportunities = [
            (
                "Operating deposits",
                money(deposit_opportunity, 1),
                "Potential additional operating balance consolidation",
            ),
            (
                "Treasury / payments",
                money(treasury_fee_opportunity),
                "Illustrative treasury, payments or liquidity opportunity",
            ),
            (
                "Available facility",
                money(undrawn_availability, 1),
                "Remaining undrawn liquidity after the scenario",
            ),
            (
                "Relationship revenue",
                money(relationship_revenue_est),
                "Illustrative annualized relationship value",
            ),
        ]

        for label, value, note in opportunities:
            render_html(
                f"""
                <div class="client-card">
                    <div class="mini-label">{label}</div>
                    <div class="mini-value">{value}</div>
                    <div style="
                        color:{MUTED};
                        font-size:14px;
                        line-height:1.45;
                        margin-top:4px;
                    ">
                        {note}
                    </div>
                </div>
                """
            )

        st.markdown("")

        render_html(
            """
            <div class="section-card">
                <div class="section-title">Suggested Banker Actions</div>
                <div class="section-sub">
                    Next steps following the client review.
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        1. Validate financial performance
                    </div>
                    <div class="memo-copy">
                        Review latest monthly management results,
                        covenant reporting and material changes in
                        operating performance.
                    </div>
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        2. Confirm borrowing requirements
                    </div>
                    <div class="memo-copy">
                        Validate use of proceeds, expected borrowing
                        duration and the client's working-capital cycle.
                    </div>
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        3. Deepen the operating relationship
                    </div>
                    <div class="memo-copy">
                        Discuss operating-account concentration,
                        deposits, payments and cash management needs.
                    </div>
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        4. Align pricing with total relationship
                    </div>
                    <div class="memo-copy">
                        Consider risk, utilization, liquidity,
                        ancillary products and total relationship value.
                    </div>
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        5. Establish monitoring cadence
                    </div>
                    <div class="memo-copy">
                        Schedule a 90-day review with clear financial,
                        credit and relationship milestones.
                    </div>
                </div>
            </div>
            """
        )


# ============================================================
# TAB 2
# ============================================================

with tab2:

    st.markdown("")

    c1, c2 = st.columns(
        [1.08, 1],
        gap="large",
    )

    with c1:

        render_html(
            """
            <div class="section-card">
                <div class="section-title">Covenant Headroom</div>
                <div class="section-sub">
                    Compare scenario performance with illustrative
                    underwriting thresholds.
                </div>
            </div>
            """
        )

        covenant_data = pd.DataFrame(
            {
                "Metric": [
                    "Debt / EBITDA",
                    "DSCR",
                    "Current Ratio",
                ],
                "Actual": [
                    ratio(stress_leverage),
                    ratio(stress_dscr),
                    ratio(current_ratio),
                ],
                "Threshold": [
                    "≤ 3.75x",
                    "≥ 1.20x",
                    "≥ 1.25x",
                ],
                "Status": [
                    (
                        "Within limit"
                        if stress_leverage <= covenant_limit
                        else "Breach"
                    ),
                    (
                        "Above floor"
                        if stress_dscr >= dscr_floor
                        else "Breach"
                    ),
                    (
                        "Above floor"
                        if current_ratio >= current_ratio_floor
                        else "Breach"
                    ),
                ],
            }
        )

        st.dataframe(
            covenant_data,
            hide_index=True,
            use_container_width=True,
        )

        st.markdown("")

        render_html(
            """
            <div class="section-card">
                <div class="section-title">Debt Capacity Bridge</div>
                <div class="section-sub">
                    Illustrative maximum debt supported at the leverage
                    threshold compared with stressed debt.
                </div>
            </div>
            """
        )

        debt_capacity_data = pd.DataFrame(
            {
                "Measure": [
                    "Stressed debt",
                    "Max debt at 3.75x",
                    "Headroom",
                ],
                "Value": [
                    stress_debt,
                    max_debt_at_leverage,
                    debt_capacity_headroom,
                ],
            }
        )

        fig = go.Figure(
            go.Bar(
                x=debt_capacity_data["Measure"],
                y=debt_capacity_data["Value"],
                marker_color=[
                    TD_DARK,
                    TD_GREEN,
                    "#A1BCA8",
                ],
            )
        )

        fig.update_yaxes(
            tickprefix="$",
            tickformat=",.0f",
        )

        fig.update_traces(
            hovertemplate="%{x}<br>$%{y:,.0f}<extra></extra>"
        )

        st.plotly_chart(
            clean_plot(
                fig,
                height=310,
            ),
            use_container_width=True,
        )

    with c2:

        render_html(
            """
            <div class="section-card">
                <div class="section-title">Stress-Test Summary</div>
                <div class="section-sub">
                    How selected assumptions flow through the
                    borrower's credit profile.
                </div>
            </div>
            """
        )

        stress_summary = pd.DataFrame(
            [
                [
                    "Revenue",
                    money(revenue, 1),
                    money(stress_revenue, 1),
                ],
                [
                    "EBITDA",
                    money(ebitda, 1),
                    money(stress_ebitda, 1),
                ],
                [
                    "Debt",
                    money(debt, 1),
                    money(stress_debt, 1),
                ],
                [
                    "Debt / EBITDA",
                    ratio(row["Debt/EBITDA"]),
                    ratio(stress_leverage),
                ],
                [
                    "DSCR",
                    ratio(row["DSCR"]),
                    ratio(stress_dscr),
                ],
                [
                    "Facility Utilization",
                    pct(utilization, 0),
                    pct(facility_utilization, 0),
                ],
            ],
            columns=[
                "Metric",
                "Base",
                "Scenario",
            ],
        )

        st.dataframe(
            stress_summary,
            hide_index=True,
            use_container_width=True,
        )

        st.markdown("")

        render_html(
            f"""
            <div class="section-card">
                <div class="section-title">Credit Memo Summary</div>
                <div class="section-sub">
                    Illustrative underwriting assessment based on
                    the selected scenario.
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        Business Performance
                    </div>
                    <div class="memo-copy">
                        {row["Industry"]} borrower generating
                        <strong>{money(revenue, 1)}</strong>
                        of annual revenue and a current EBITDA margin
                        of <strong>{pct(base_margin)}</strong>.
                        Under the selected scenario, revenue is estimated
                        at <strong>{money(stress_revenue, 1)}</strong>
                        and EBITDA at
                        <strong>{money(stress_ebitda, 1)}</strong>.
                    </div>
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        Leverage
                    </div>
                    <div class="memo-copy">
                        Stressed Debt / EBITDA is
                        <strong>{ratio(stress_leverage)}</strong>
                        compared with an illustrative maximum leverage
                        threshold of
                        <strong>{ratio(covenant_limit)}</strong>.
                        This provides approximately
                        <strong>{max(leverage_headroom, 0):.2f}x</strong>
                        of leverage headroom.
                    </div>
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        Debt Service Capacity
                    </div>
                    <div class="memo-copy">
                        Stressed DSCR is
                        <strong>{ratio(stress_dscr)}</strong>
                        versus an illustrative minimum requirement
                        of <strong>{ratio(dscr_floor)}</strong>.
                        The scenario therefore provides approximately
                        <strong>{max(dscr_headroom, 0):.2f}x</strong>
                        of coverage above the minimum threshold.
                    </div>
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        Liquidity & Facility Usage
                    </div>
                    <div class="memo-copy">
                        The borrower maintains a current ratio of
                        <strong>{ratio(current_ratio)}</strong>.
                        Following the selected incremental draw,
                        facility utilization is estimated at
                        <strong>{pct(facility_utilization, 0)}</strong>,
                        leaving approximately
                        <strong>{money(undrawn_availability, 1)}</strong>
                        of undrawn availability.
                    </div>
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        Relationship Opportunity
                    </div>
                    <div class="memo-copy">
                        The client currently maintains approximately
                        <strong>{money(deposits, 1)}</strong>
                        of deposits, with an estimated
                        <strong>{money(deposit_opportunity, 1)}</strong>
                        opportunity to consolidate additional operating
                        balances. Treasury, payments and cash management
                        needs should also be evaluated as part of the
                        broader client relationship.
                    </div>
                </div>

                <div class="memo-rec">
                    <div class="memo-rec-label">
                        Credit Recommendation
                    </div>
                    <div class="memo-rec-title">
                        {recommendation}
                    </div>
                    <div class="memo-rec-copy">
                        {rec_text}
                    </div>
                </div>
            </div>
            """
        )


# ============================================================
# TAB 3
# ============================================================

with tab3:

    st.markdown("")

    st.markdown("### Working-Capital Diagnostic")

    st.caption(
        "Commercial bankers assess the operating cash cycle alongside "
        "profitability to understand liquidity needs and borrowing behaviour."
    )

    ar_days = max(
        25,
        round(ccc * 0.60),
    )

    inventory_days = max(
        10,
        round(ccc * 0.50),
    )

    payable_days = max(
        15,
        round(
            ar_days
            + inventory_days
            - ccc
        ),
    )

    w1, w2, w3, w4 = st.columns(4)

    with w1:
        metric_card(
            "Receivable Days",
            f"{ar_days} days",
            "Illustrative customer collection cycle",
        )

    with w2:
        metric_card(
            "Inventory Days",
            f"{inventory_days} days",
            "Illustrative inventory holding period",
        )

    with w3:
        metric_card(
            "Payable Days",
            f"{payable_days} days",
            "Illustrative supplier payment cycle",
        )

    with w4:
        metric_card(
            "Cash Conversion Cycle",
            f"{int(ccc)} days",
            "Net operating cash tied up",
        )

    st.markdown("")

    left, right = st.columns(
        [1.25, 1],
        gap="large",
    )

    with left:

        render_html(
            """
            <div class="section-card">
                <div class="section-title">
                    Operating Liquidity Trend
                </div>
                <div class="section-sub">
                    Illustrative monthly borrowing and deposit balances.
                </div>
            </div>
            """
        )

        months = pd.date_range(
            start="2026-01-01",
            periods=8,
            freq="M",
        )

        seasonal = np.array(
            [
                0.76,
                0.80,
                0.84,
                0.89,
                0.93,
                0.88,
                0.82,
                0.79,
            ]
        )

        borrowing_line = stress_drawn * seasonal

        deposit_line = (
            deposits
            * np.array(
                [
                    0.94,
                    1.02,
                    0.91,
                    0.98,
                    1.08,
                    1.04,
                    1.12,
                    1.16,
                ]
            )
        )

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=months,
                y=borrowing_line,
                mode="lines+markers",
                name="Borrowings",
                line=dict(
                    color=TD_DARK,
                    width=3,
                ),
                marker=dict(
                    size=7,
                ),
            )
        )

        fig.add_trace(
            go.Scatter(
                x=months,
                y=deposit_line,
                mode="lines+markers",
                name="Deposits",
                line=dict(
                    color=TD_GREEN,
                    width=3,
                ),
                marker=dict(
                    size=7,
                ),
            )
        )

        fig.update_layout(
            legend=dict(
                orientation="h",
                y=1.12,
                x=0,
            )
        )

        fig.update_yaxes(
            tickprefix="$",
            tickformat=",.0f",
        )

        st.plotly_chart(
            clean_plot(
                fig,
                height=340,
                showlegend=True,
            ),
            use_container_width=True,
        )

    with right:

        render_html(
            f"""
            <div class="section-card">
                <div class="section-title">
                    Working-Capital Interpretation
                </div>

                <div class="section-sub">
                    How operating efficiency can influence liquidity requirements,
                    facility usage and the broader banking relationship.
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        Cash Conversion Cycle
                    </div>
                    <div class="memo-copy">
                        The borrower has an illustrative cash conversion cycle of
                        <strong>{int(ccc)} days</strong>. This represents the approximate
                        period between deploying cash into operations and recovering that
                        cash through customer collections.
                    </div>
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        Borrowing Dependence
                    </div>
                    <div class="memo-copy">
                        Under the selected scenario, facility utilization is approximately
                        <strong>{pct(facility_utilization, 0)}</strong>. Higher utilization
                        may indicate greater dependence on bank liquidity to fund normal
                        operating requirements.
                    </div>
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        Receivables
                    </div>
                    <div class="memo-copy">
                        Receivable days are estimated at
                        <strong>{ar_days} days</strong>. Slower customer collections can
                        increase working-capital requirements even when reported earnings
                        remain healthy.
                    </div>
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        Inventory
                    </div>
                    <div class="memo-copy">
                        Inventory is held for approximately
                        <strong>{inventory_days} days</strong>. A material increase in
                        inventory days could absorb cash and increase borrowing requirements.
                    </div>
                </div>

                <div class="memo-section">
                    <div class="memo-heading">
                        Relationship Opportunity
                    </div>
                    <div class="memo-copy">
                        Consolidating operating deposits and reviewing receivables,
                        payments and liquidity-management processes may improve visibility
                        into cash flows while creating opportunities to deepen the overall
                        banking relationship.
                    </div>
                </div>
            </div>
            """
        )

        st.markdown("")

        if TD_COMMERCIAL.exists():
            st.image(
                str(TD_COMMERCIAL),
                use_container_width=True,
            )


# ============================================================
# TAB 4
# ============================================================

with tab4:

    st.markdown("")

    st.markdown("### Portfolio Triage")

    st.caption(
        "Compare borrowers to prioritize client reviews, "
        "credit work and relationship-management activity."
    )

    portfolio = clients.copy()

    portfolio["Revenue"] = portfolio["Revenue"].map(
        lambda x: money(x, 1)
    )

    portfolio["EBITDA"] = portfolio["EBITDA"].map(
        lambda x: money(x, 1)
    )

    portfolio["Debt"] = portfolio["Debt"].map(
        lambda x: money(x, 1)
    )

    portfolio["Deposits"] = portfolio["Deposit Balance"].map(
        lambda x: money(x, 1)
    )

    portfolio["Debt / EBITDA"] = portfolio["Debt/EBITDA"].map(
        ratio
    )

    portfolio["DSCR"] = portfolio["DSCR"].map(
        ratio
    )

    portfolio["Utilization"] = portfolio["Facility Utilization"].map(
        lambda x: pct(x, 0)
    )

    st.dataframe(
        portfolio[
            [
                "Client",
                "Industry",
                "Revenue",
                "EBITDA",
                "Debt",
                "Debt / EBITDA",
                "DSCR",
                "Utilization",
                "Deposits",
                "CCC Days",
                "Risk",
            ]
        ],
        hide_index=True,
        use_container_width=True,
        height=280,
    )

    st.markdown("")

    p1, p2 = st.columns(
        [1.15, 1],
        gap="large",
    )

    with p1:

        render_html(
            """
            <div class="section-card">
                <div class="section-title">Credit Risk Map</div>
                <div class="section-sub">
                    Portfolio positioning across leverage and
                    debt service coverage.
                </div>
            </div>
            """
        )

        base = clients.copy()

        point_colours = [
            TD_GREEN if risk == "Low" else AMBER
            for risk in base["Risk"]
        ]

        point_sizes = (
            (base["Facility"] / 1_000_000) * 1.7
            + 12
        )

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=base["Debt/EBITDA"],
                y=base["DSCR"],
                mode="markers+text",
                text=base["Client"],
                textposition="top center",
                marker=dict(
                    size=point_sizes,
                    color=point_colours,
                    line=dict(
                        width=1,
                        color="white",
                    ),
                ),
                hovertemplate=(
                    "<b>%{text}</b>"
                    "<br>Debt / EBITDA: %{x:.2f}x"
                    "<br>DSCR: %{y:.2f}x"
                    "<extra></extra>"
                ),
            )
        )

        fig.add_vline(
            x=covenant_limit,
            line_dash="dash",
            line_color="#A66A1E",
        )

        fig.add_hline(
            y=dscr_floor,
            line_dash="dash",
            line_color="#A66A1E",
        )

        fig.update_xaxes(
            title="Debt / EBITDA",
        )

        fig.update_yaxes(
            title="DSCR",
        )

        st.plotly_chart(
            clean_plot(
                fig,
                height=390,
            ),
            use_container_width=True,
        )

    with p2:

        render_html(
            """
            <div class="section-card">
                <div class="section-title">Deposit Relationships</div>
                <div class="section-sub">
                    Current operating deposit balances across the
                    synthetic client portfolio.
                </div>
            </div>
            """
        )

        fig = go.Figure(
            go.Bar(
                x=clients["Client"],
                y=clients["Deposit Balance"],
                marker_color=[
                    TD_GREEN,
                    "#3A7952",
                    "#5D8E69",
                    "#80A386",
                    "#A2B9A5",
                ],
            )
        )

        fig.update_yaxes(
            tickprefix="$",
            tickformat=",.0f",
        )

        fig.update_xaxes(
            tickangle=-22,
        )

        fig.update_traces(
            hovertemplate="%{x}<br>$%{y:,.0f}<extra></extra>"
        )

        st.plotly_chart(
            clean_plot(
                fig,
                height=390,
            ),
            use_container_width=True,
        )


# ============================================================
# EXPORT
# ============================================================

st.markdown("---")

export_data = pd.DataFrame(
    {
        "Metric": [
            "Client",
            "Industry",
            "Revenue",
            "EBITDA",
            "Scenario Revenue",
            "Scenario EBITDA",
            "Debt",
            "Scenario Debt",
            "Base Debt / EBITDA",
            "Scenario Debt / EBITDA",
            "Base DSCR",
            "Scenario DSCR",
            "Facility",
            "Scenario Facility Utilization",
            "Current Ratio",
            "Deposits",
            "Potential Deposit Growth",
            "Illustrative Relationship Revenue",
            "Recommendation",
        ],
        "Value": [
            selected_client,
            row["Industry"],
            revenue,
            ebitda,
            stress_revenue,
            stress_ebitda,
            debt,
            stress_debt,
            row["Debt/EBITDA"],
            stress_leverage,
            row["DSCR"],
            stress_dscr,
            facility,
            facility_utilization,
            current_ratio,
            deposits,
            deposit_opportunity,
            relationship_revenue_est,
            recommendation,
        ],
    }
)

csv = export_data.to_csv(
    index=False,
).encode("utf-8")

download_col, disclaimer_col = st.columns(
    [1, 3.2],
    gap="large",
)

with download_col:

    st.download_button(
        "Export client snapshot",
        data=csv,
        file_name=(
            selected_client
            .lower()
            .replace(" ", "_")
            + "_credit_snapshot.csv"
        ),
        mime="text/csv",
        use_container_width=True,
    )

with disclaimer_col:

    render_html(
        """
        <div class="footer-note">
            Independent portfolio demonstration using synthetic data.
            Created to demonstrate commercial banking analysis, credit
            judgment, relationship economics, working capital analysis
            and executive communication.

            This project is not affiliated with, endorsed by or
            commissioned by TD Bank Group.
        </div>
        """
    )