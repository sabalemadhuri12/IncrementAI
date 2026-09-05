# IncrementAI 🚀

### AI-Powered Incremental Revenue Optimization

> **Don't just predict what a customer will buy. Predict what action will make them spend more.**

IncrementAI is an AI-powered revenue intelligence system that identifies customers who are most likely to generate **additional revenue because of a targeted intervention**.

Instead of simply predicting customer purchases, IncrementAI estimates the difference between:

- **Probability of purchase without an intervention**
- **Probability of purchase with an intervention**
- **Uplift = P(Purchase | Action) − P(Purchase | No Action)**

The system then recommends the most appropriate action for each customer and estimates the potential incremental revenue.

---

## 🎯 Problem

Traditional recommendation systems answer:

> "What is this customer likely to buy?"

But this does not answer the more important business question:

> **"What action should I take to actually increase this customer's spending?"**

Businesses often send discounts, reminders, upsells, and promotional campaigns to customers who would have purchased anyway.

This creates:

- Unnecessary discounts
- Wasted marketing budget
- Lower margins
- Poor campaign targeting
- Missed opportunities for incremental revenue

---

## 💡 Solution

IncrementAI uses **uplift-style treatment-control modeling** to estimate the incremental impact of an intervention on each customer.

For every customer, the system estimates:

```text
Purchase Probability Without Action
                ↓
Purchase Probability With Action
                ↓
              UPLIFT
                ↓
       AI Action Recommendation
                ↓
       Incremental Revenue Estimate
```

The system then recommends the most appropriate action:

| Uplift | Recommended Action |
|---|---|
| < 5% | No Action |
| 5% – 15% | Reminder |
| 15% – 30% | Upsell / Cross-sell |
| > 30% | Personalized Offer |

---

## 📊 Key Features

### 1. Customer-Level Uplift Prediction

Predicts:

- Probability of purchase without intervention
- Probability of purchase with intervention
- Estimated uplift

### 2. AI Action Recommendation

Automatically recommends:

- No Action
- Reminder
- Upsell
- Cross-sell
- Personalized Offer

### 3. Incremental Revenue Estimation

The system estimates:

```text
Incremental Revenue
= Uplift × Average Order Value
```

This helps merchants prioritize customers with the highest potential revenue opportunity.

### 4. Customer Intelligence

Merchants can select an individual customer and view:

- Customer profile
- Purchase history
- Spending behavior
- AI prediction
- Recommended action
- Expected incremental revenue
- AI-generated explanation

### 5. Campaign Simulation

The dashboard includes a simulated:

**Launch AI Campaign**

In a production system, this could connect the AI recommendation to a merchant's campaign channel and payment/checkout flow.

### 6. Promotional Budget Protection

Customers predicted to require no intervention can be excluded from unnecessary promotional offers.

For this MVP, promotional budget protection is represented using an illustrative estimate.

---

## 🧠 How IncrementAI Works

```text
                 CUSTOMER DATA
                      │
                      ▼
          ┌───────────────────────┐
          │ Feature Preparation   │
          │                       │
          │ Age                   │
          │ City                  │
          │ Previous Purchases    │
          │ Total Spend           │
          │ Average Order Value   │
          │ Days Since Purchase   │
          │ Category              │
          │ Discount Response     │
          └───────────┬───────────┘
                      │
                      ▼
        ┌─────────────────────────────┐
        │ Treatment Model             │
        │ Customers exposed to action │
        └──────────────┬──────────────┘
                       │
                       ▼
              P(Purchase | Action)
                       │
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
 P(Purchase | Action)       P(Purchase | No Action)
        │                             │
        └──────────────┬──────────────┘
                       │
                       ▼
                UPLIFT ESTIMATE
                       │
                       ▼
              AI ACTION ENGINE
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Reminder      Upsell    Personalized
                                Offer
                       │
                       ▼
            INCREMENTAL REVENUE
                       │
                       ▼
             CAMPAIGN SIMULATION
```

---

## 🏗️ Project Architecture

```text
IncrementAI
│
├── app.py
│   └── Streamlit dashboard and user interface
│
├── uplift_model.py
│   ├── Feature preparation
│   ├── Treatment model
│   ├── Control model
│   ├── Uplift calculation
│   ├── Action recommendation
│   ├── Revenue estimation
│   └── AI explanation generation
│
├── data/
│   └── customers.csv
│       └── Synthetic customer dataset
│
├── requirements.txt
│   └── Python dependencies
│
├── .gitignore
│
└── README.md
```

---

## 🛠️ Tech Stack

### Dashboard

- Streamlit
- Plotly

### Machine Learning

- Python
- Scikit-learn
- Random Forest
- Treatment-Control Modeling
- Uplift-style Modeling

### Data Processing

- Pandas
- NumPy

### Development

- VS Code
- Git
- GitHub

---

## 📈 Dashboard

The IncrementAI dashboard provides a merchant-focused revenue intelligence interface.

### Main KPIs

- Customers Analyzed
- Opportunities Found
- Expected Incremental Revenue
- Average Uplift
- Promotional Budget Protected

### Visualizations

- Revenue Opportunity by Action
- AI Action Distribution
- Customer Opportunity Ranking

### Customer Intelligence

The merchant can select a customer to see the AI recommendation and understand:

> **Why should I take this action for this customer?**

---

## 🧪 Example

For a customer with:

```text
Probability without action = 38%
Probability with action    = 78%
```

The estimated uplift is:

```text
78% − 38% = 40%
```

If the customer's average order value is:

```text
₹6,750
```

The estimated incremental revenue opportunity is:

```text
40% × ₹6,750 = ₹2,700
```

Therefore, IncrementAI may recommend:

```text
Personalized Offer
```

The key insight is that the system is not simply asking whether the customer will purchase.

It is asking whether the **intervention changes the probability of purchase enough to justify taking action**.

---

## 🚀 Running the Project Locally

Follow these steps to run IncrementAI on your computer.

### Prerequisites

Make sure you have:

- Python 3.10 or later
- Git
- VS Code (recommended)

### 1. Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/sabalemadhuri12/IncrementAI.git
```

Then enter the project folder:

```bash
cd IncrementAI
```

### 2. Create a virtual environment

On Windows, run:

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

For PowerShell:

```powershell
.venv\Scripts\activate
```

After activation, you should see `(.venv)` at the beginning of your terminal prompt.

### 4. Install the required libraries

Run:

```bash
pip install -r requirements.txt
```

### 5. Run the dashboard

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📂 Dataset

The current MVP uses a **synthetic customer dataset** containing customer behavior and treatment information.

Example features include:

```text
customer_id
age
city
previous_purchases
total_spend
avg_order_value
days_since_purchase
category
discount_response
treatment
purchased_after
```

The synthetic dataset is used to demonstrate the end-to-end product and modeling workflow without exposing real customer data.

---

## ⚠️ MVP Limitations

This project is a hackathon MVP designed to demonstrate the product concept and technical workflow.

Current limitations include:

- Synthetic dataset
- Small dataset size
- Simplified treatment/control modeling
- Estimated rather than production-grade causal effects
- Simulated campaign execution
- Simulated payment/checkout integration
- No real-time merchant transaction pipeline

Therefore, the current revenue figures should be interpreted as **model estimates for demonstration**, not guaranteed business outcomes.

---

## 🔮 Future Scope

### 1. Real Payment Integration

Connect the system with a payment infrastructure such as Razorpay to observe:

```text
Customer
   ↓
AI Recommendation
   ↓
Campaign
   ↓
Checkout
   ↓
Payment
   ↓
Actual Revenue
```

### 2. Agentic Revenue Optimization

A future AI agent could autonomously:

1. Identify high-potential customers
2. Select the optimal intervention
3. Generate personalized messaging
4. Launch the campaign
5. Route the customer to checkout
6. Observe payment behavior
7. Measure incremental revenue
8. Learn from the result
9. Improve future recommendations

### 3. Real-Time Decision Making

The system could make decisions based on:

- Recent purchases
- Payment behavior
- Cart activity
- Customer lifetime value
- Product affinity
- Campaign history
- Real-time checkout signals

### 4. Profit Optimization

Instead of optimizing only revenue, the system can optimize:

```text
Incremental Profit
=
Incremental Revenue
−
Campaign Cost
−
Discount Cost
```

### 5. Continuous Learning

Actual campaign outcomes can be fed back into the model:

```text
Prediction
    ↓
Action
    ↓
Customer Response
    ↓
Revenue
    ↓
Learning
    ↓
Better Prediction
```

---

## 🎯 Business Impact

IncrementAI is designed around a simple principle:

> **Do not spend money influencing customers who would buy anyway.**

Instead, focus interventions on customers where the AI estimates that the action itself can create additional revenue.

This can help merchants:

- Increase conversion
- Reduce unnecessary discounts
- Improve marketing efficiency
- Prioritize high-value opportunities
- Increase incremental revenue
- Move from reactive campaigns to AI-driven decision making

---

## 🏆 Why IncrementAI?

Traditional analytics:

> **"Who is likely to buy?"**

Traditional recommendation:

> **"What should we recommend?"**

IncrementAI:

> **"Which customer should we influence, what should we do, and how much additional revenue could that action create?"**

That shift from **prediction to action** is the core idea behind IncrementAI.

---

## 👩‍💻 Author

**Madhuri Sabale**

BTech Computer Science Engineering

---

## 📌 Project Status

**MVP Complete ✅**

The current version demonstrates the workflow from:

```text
Customer Data
      ↓
Uplift Estimation
      ↓
AI Recommendation
      ↓
Revenue Opportunity
      ↓
Merchant Dashboard
      ↓
Campaign Simulation
```

---

## 📄 Disclaimer

This project is a hackathon MVP created for demonstrating AI-powered incremental revenue optimization.

The current implementation uses synthetic data and simulated campaign/payment flows. Production deployment would require real merchant data, robust causal inference validation, privacy and security controls, real campaign integrations, and production payment infrastructure.