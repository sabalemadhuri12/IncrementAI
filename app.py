import streamlit as st
import pandas as pd
import plotly.express as px

from uplift_model import (
    calculate_uplift,
    recommend_action,
    calculate_revenue_opportunity,
    generate_explanation,
    calculate_discount_avoided
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="IncrementAI | Revenue Intelligence",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM FINTECH STYLING
# =========================================================

st.markdown("""
<style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background-color: #f5f7fb;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1450px;
    }

    h1, h2, h3 {
        color: #14213d !important;
    }

    p, label {
        color: #526071;
    }


    /* ---------- SIDEBAR ---------- */

    [data-testid="stSidebar"] {
        background-color: #101828;
    }

    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    .sidebar-brand {
        font-size: 24px;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 4px;
    }

    .sidebar-subtitle {
        font-size: 12px;
        color: #98a2b3 !important;
        margin-bottom: 28px;
    }

    .sidebar-status {
        background: #162a24;
        border: 1px solid #1f4d3c;
        border-radius: 10px;
        padding: 12px;
        margin-top: 25px;
        font-size: 12px;
    }

    .status-dot {
        color: #32d583 !important;
        font-weight: 700;
    }


    /* ---------- HEADER ---------- */

    .top-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #ffffff;
        border: 1px solid #e4e7ec;
        border-radius: 16px;
        padding: 22px 26px;
        margin-bottom: 22px;
        box-shadow: 0 2px 8px rgba(16, 24, 40, 0.04);
    }

    .brand-title {
        font-size: 28px;
        font-weight: 800;
        color: #14213d;
        margin: 0;
    }

    .brand-subtitle {
        font-size: 13px;
        color: #667085;
        margin-top: 4px;
    }

    .live-badge {
        background: #ecfdf3;
        color: #027a48;
        border: 1px solid #abefc6;
        padding: 8px 13px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
    }


    /* ---------- KPI CARDS ---------- */

    .kpi-card {
        background: #ffffff;
        border: 1px solid #e4e7ec;
        border-radius: 14px;
        padding: 19px 20px;
        min-height: 115px;
        box-shadow: 0 2px 7px rgba(16, 24, 40, 0.035);
    }

    .kpi-label {
        color: #667085;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 9px;
    }

    .kpi-value {
        color: #14213d;
        font-size: 27px;
        font-weight: 800;
        letter-spacing: -0.5px;
    }

    .kpi-positive {
        color: #039855;
    }

    .kpi-small {
        color: #667085;
        font-size: 11px;
        margin-top: 5px;
    }


    /* ---------- SECTION CARDS ---------- */

    .section-card {
        background: #ffffff;
        border: 1px solid #e4e7ec;
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 2px 7px rgba(16, 24, 40, 0.035);
    }


    /* ---------- AI CARD ---------- */

    .ai-card {
        background: linear-gradient(135deg, #f0fdf4, #ffffff);
        border: 1px solid #abefc6;
        border-radius: 14px;
        padding: 22px;
        margin-top: 10px;
    }

    .ai-title {
        color: #027a48;
        font-size: 15px;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .ai-value {
        color: #14213d;
        font-size: 24px;
        font-weight: 800;
    }


    /* ---------- DIVIDER ---------- */

    .soft-divider {
        height: 1px;
        background: #eaecf0;
        margin: 28px 0;
    }


    /* ---------- TABLE ---------- */

    [data-testid="stDataFrame"] {
        border: 1px solid #e4e7ec;
        border-radius: 12px;
        overflow: hidden;
    }


    /* ---------- BUTTON ---------- */

    .stButton > button {
        width: 100%;
        border-radius: 9px;
        border: none;
        background: #14213d;
        color: white;
        font-weight: 700;
        padding: 11px 20px;
    }

    .stButton > button:hover {
        background: #243b64;
        color: white;
    }


    /* ---------- SELECTBOX ---------- */

    div[data-baseweb="select"] > div {
        border-radius: 9px;
        border-color: #d0d5dd;
        background: white;
    }


    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #98a2b3;
        font-size: 11px;
        padding-top: 25px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    df = pd.read_csv("data/customers.csv")

    results = calculate_uplift(df)

    results["recommended_action"] = results.apply(
        recommend_action,
        axis=1
    )

    results["incremental_revenue"] = results.apply(
        calculate_revenue_opportunity,
        axis=1
    )

    results["discount_avoided"] = results.apply(
        calculate_discount_avoided,
        axis=1
    )

    return results


df = load_data()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-brand">📈 IncrementAI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">Revenue Intelligence Platform</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Navigation")

    st.markdown("▸ Overview")
    st.markdown("▸ Customer Intelligence")
    st.markdown("▸ AI Actions")
    st.markdown("▸ Campaign Opportunities")

    st.markdown(
        """
        <div class="sidebar-status">
            <span class="status-dot">● AI ENGINE LIVE</span><br>
            <span style="color:#98a2b3 !important;">
            Uplift scoring active
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.caption("MVP • Incremental Revenue Optimization")


# =========================================================
# HEADER
# =========================================================

# =========================================================
# HEADER
# =========================================================

header_left, header_right = st.columns([5, 1])

with header_left:

    st.markdown(
        """
        <div class="brand-title">IncrementAI</div>
        <div class="brand-subtitle">
            AI-powered incremental revenue optimization for merchants
        </div>
        """,
        unsafe_allow_html=True
    )

with header_right:

    st.success("● AI ENGINE LIVE")

# =========================================================
# KEY METRICS
# =========================================================

total_customers = len(df)

opportunities = len(
    df[df["uplift"] > 0.05]
)

total_revenue = df["incremental_revenue"].sum()

total_discount_avoided = df["discount_avoided"].sum()

avg_uplift = df["uplift"].mean()


st.markdown("### Revenue Intelligence")

c1, c2, c3, c4, c5 = st.columns(5)


with c1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">CUSTOMERS ANALYZED</div>
            <div class="kpi-value">{total_customers:,}</div>
            <div class="kpi-small">Customer profiles scored</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with c2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">AI OPPORTUNITIES</div>
            <div class="kpi-value">{opportunities:,}</div>
            <div class="kpi-small">High-impact customers</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with c3:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">INCREMENTAL REVENUE</div>
            <div class="kpi-value kpi-positive">
                ₹{total_revenue:,.0f}
            </div>
            <div class="kpi-small">Estimated opportunity</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with c4:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">AVERAGE UPLIFT</div>
            <div class="kpi-value">
                {avg_uplift * 100:.1f}%
            </div>
            <div class="kpi-small">Estimated incremental effect</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with c5:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">DISCOUNTS AVOIDED</div>
            <div class="kpi-value kpi-positive">
                ₹{total_discount_avoided:,.0f}
            </div>
            <div class="kpi-small">Promotional budget protected</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# CHARTS
# =========================================================

st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)

chart1, chart2 = st.columns(2)


with chart1:

    st.markdown("### 💰 Revenue Opportunity")

    action_revenue = (
        df.groupby("recommended_action")["incremental_revenue"]
        .sum()
        .reset_index()
        .sort_values("incremental_revenue", ascending=False)
    )

    fig_revenue = px.bar(
        action_revenue,
        x="recommended_action",
        y="incremental_revenue",
        labels={
            "recommended_action": "AI Action",
            "incremental_revenue": "Expected Revenue (₹)"
        }
    )

    fig_revenue.update_layout(
        height=360,
        margin=dict(l=10, r=10, t=20, b=10),
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#526071"),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="#eaecf0")
    )

    st.plotly_chart(
        fig_revenue,
        use_container_width=True
    )


with chart2:

    st.markdown("### 🎯 AI Action Distribution")

    action_counts = (
        df["recommended_action"]
        .value_counts()
        .reset_index()
    )

    action_counts.columns = [
        "recommended_action",
        "customer_count"
    ]

    fig_actions = px.bar(
        action_counts,
        x="recommended_action",
        y="customer_count",
        labels={
            "recommended_action": "AI Action",
            "customer_count": "Customers"
        }
    )

    fig_actions.update_layout(
        height=360,
        margin=dict(l=10, r=10, t=20, b=10),
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#526071"),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="#eaecf0")
    )

    st.plotly_chart(
        fig_actions,
        use_container_width=True
    )


# =========================================================
# CUSTOMER OPPORTUNITIES
# =========================================================

st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)

st.markdown("### 🎯 Top Customer Opportunities")

st.caption(
    "Customers ranked by estimated incremental revenue opportunity."
)


display_df = df.sort_values(
    "incremental_revenue",
    ascending=False
).copy()

display_df["uplift_percent"] = (
    display_df["uplift"] * 100
).round(1)

display_df = display_df[
    [
        "customer_id",
        "category",
        "uplift_percent",
        "recommended_action",
        "avg_order_value",
        "incremental_revenue"
    ]
]

display_df.columns = [
    "Customer",
    "Category",
    "Uplift %",
    "Recommended Action",
    "Avg Order Value",
    "Expected Revenue"
]

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# CUSTOMER INTELLIGENCE
# =========================================================

st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)

st.markdown("### 🔎 Customer Intelligence")

st.caption(
    "Understand why IncrementAI recommends a specific action."
)

customer_list = df["customer_id"].tolist()

selected_customer = st.selectbox(
    "Select Customer",
    customer_list
)

customer = df[
    df["customer_id"] == selected_customer
].iloc[0]


# Customer overview
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">PREVIOUS PURCHASES</div>
            <div class="kpi-value">
                {int(customer["previous_purchases"])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">TOTAL SPEND</div>
            <div class="kpi-value">
                ₹{customer["total_spend"]:,.0f}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">AVERAGE ORDER</div>
            <div class="kpi-value">
                ₹{customer["avg_order_value"]:,.0f}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">DAYS SINCE PURCHASE</div>
            <div class="kpi-value">
                {int(customer["days_since_purchase"])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# AI PREDICTION
# =========================================================

st.markdown("### 🤖 AI Prediction")

p1, p2, p3 = st.columns(3)

with p1:

    st.markdown(
        f"""
        <div class="section-card">
            <div class="kpi-label">
                PURCHASE PROBABILITY — NO ACTION
            </div>
            <div class="ai-value">
                {customer["prob_without_action"] * 100:.1f}%
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with p2:

    st.markdown(
        f"""
        <div class="section-card">
            <div class="kpi-label">
                PURCHASE PROBABILITY — WITH ACTION
            </div>
            <div class="ai-value kpi-positive">
                {customer["prob_with_action"] * 100:.1f}%
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with p3:

    st.markdown(
        f"""
        <div class="ai-card">
            <div class="ai-title">INCREMENTAL UPLIFT</div>
            <div class="ai-value">
                +{customer["uplift"] * 100:.1f}%
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# AI RECOMMENDATION
# =========================================================

st.markdown("### 🎯 AI Recommendation")

action = customer["recommended_action"]

explanation = generate_explanation(customer)

st.success(
    f"Recommended Action: {action}\n\n"
    f"{explanation}\n\n"
    f"Expected Incremental Revenue: "
    f"₹{customer['incremental_revenue']:,.0f}"
)

# =========================================================
# WHY THIS CUSTOMER
# =========================================================

st.markdown("### 🧠 Why This Customer?")

st.write(
    f"IncrementAI estimates that **{selected_customer}** has a "
    f"purchase probability of "
    f"**{customer['prob_without_action'] * 100:.1f}%** "
    f"without intervention and "
    f"**{customer['prob_with_action'] * 100:.1f}%** "
    f"with the recommended action."
)

st.write(
    f"That represents an estimated incremental uplift of "
    f"**{customer['uplift'] * 100:.1f} percentage points**, "
    f"creating an estimated revenue opportunity of "
    f"**₹{customer['incremental_revenue']:,.0f}**."
)


# =========================================================
# CAMPAIGN ACTION
# =========================================================

st.markdown("### 🚀 AI Campaign Action")

st.caption(
    "Convert the AI recommendation into an actionable campaign."
)

if st.button(
    "🚀 Launch AI Campaign",
    use_container_width=True
):

    st.success(
        f"Campaign prepared for {selected_customer}."
    )

    st.write(
        f"**Recommended Action:** "
        f"{customer['recommended_action']}"
    )

    st.write(
        f"**Target Category:** "
        f"{customer['category']}"
    )

    st.write(
        f"**Expected Incremental Revenue:** "
        f"₹{customer['incremental_revenue']:,.0f}"
    )

    st.info(
        "Production integration would connect this action "
        "to the merchant's campaign channel and route the "
        "customer toward a Razorpay checkout."
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        IncrementAI • AI-powered incremental revenue optimization • MVP
    </div>
    """,
    unsafe_allow_html=True
)