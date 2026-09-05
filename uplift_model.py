import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier


def prepare_features(df):
    """
    Prepare customer data for machine learning.
    Removes identifiers and converts categorical columns
    into numerical features.
    """

    features = df.drop(
        columns=["customer_id", "treatment", "purchased_after"]
    )

    # Convert categorical columns into numerical columns
    features = pd.get_dummies(
        features,
        columns=["city", "category"],
        drop_first=False
    )

    return features


def train_uplift_models(df):
    """
    Train two models:

    1. Treatment model:
       Predicts purchase probability when an intervention is given.

    2. Control model:
       Predicts purchase probability when no intervention is given.
    """

    X = prepare_features(df)
    y = df["purchased_after"]

    treatment_mask = df["treatment"] == 1
    control_mask = df["treatment"] == 0

    X_treatment = X[treatment_mask]
    y_treatment = y[treatment_mask]

    X_control = X[control_mask]
    y_control = y[control_mask]

    # Treatment model
    treatment_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42,
        class_weight="balanced"
    )

    treatment_model.fit(X_treatment, y_treatment)

    # Control model
    control_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42,
        class_weight="balanced"
    )

    control_model.fit(X_control, y_control)

    return treatment_model, control_model, X.columns


def calculate_uplift(df):
    """
    Calculate estimated purchase probability under:

    - Treatment
    - Control

    Uplift = Treatment probability - Control probability
    """

    treatment_model, control_model, feature_columns = train_uplift_models(df)

    X = prepare_features(df)

    # Make sure prediction columns match training columns
    X = X.reindex(columns=feature_columns, fill_value=0)

    treatment_probability = treatment_model.predict_proba(X)[:, 1]

    control_probability = control_model.predict_proba(X)[:, 1]

    # Incremental effect
    uplift = treatment_probability - control_probability

    results = df.copy()

    results["prob_without_action"] = control_probability
    results["prob_with_action"] = treatment_probability
    results["uplift"] = uplift

    return results


def recommend_action(row):
    """
    Convert the predicted uplift into a business action.
    """

    uplift = row["uplift"]
    category = row["category"]

    # Negative or very small uplift:
    # do not waste money on an intervention.
    if uplift < 0.05:
        return "No Action"

    # Moderate uplift:
    # a low-cost reminder is sufficient.
    elif uplift < 0.15:
        return "Reminder"

    # High uplift:
    # recommend a product-specific growth action.
    elif uplift < 0.30:
        if category == "Electronics":
            return "Upsell"
        else:
            return "Cross-sell"

    # Very high uplift:
    # personalized offer is justified.
    else:
        return "Personalized Offer"


def calculate_revenue_opportunity(row):
    """
    Estimate the additional revenue that could be generated
    by targeting a customer with the recommended action.
    """

    # Only positive uplift represents an opportunity.
    if row["uplift"] <= 0:
        return 0.0

    # Use the customer's historical average order value
    # as an estimate of the potential transaction value.
    expected_revenue = row["uplift"] * row["avg_order_value"]

    return round(expected_revenue, 2)

def generate_explanation(row):
    """
    Generate a simple business explanation for
    the recommended AI action.
    """

    action = row["recommended_action"]
    uplift = row["uplift"]
    spend = row["total_spend"]
    purchases = row["previous_purchases"]
    discount_response = row["discount_response"]

    if action == "No Action":

        return (
            f"IncrementAI recommends no intervention because "
            f"the estimated incremental uplift is only "
            f"{uplift * 100:.1f}%. Spending promotional budget "
            f"on this customer is unlikely to create enough "
            f"additional value."
        )

    elif action == "Reminder":

        return (
            f"This customer has made {purchases} previous purchases "
            f"and has spent ₹{spend:,.0f}. The estimated uplift is "
            f"{uplift * 100:.1f}%, so a low-cost reminder is "
            f"recommended instead of an expensive discount."
        )

    elif action == "Upsell":

        return (
            f"This customer has strong purchase history and an "
            f"estimated incremental uplift of {uplift * 100:.1f}%. "
            f"IncrementAI recommends an upsell to increase the "
            f"value of the next transaction."
        )

    elif action == "Cross-sell":

        return (
            f"This customer has an estimated incremental uplift "
            f"of {uplift * 100:.1f}%. Their purchase history suggests "
            f"potential for an additional product, so IncrementAI "
            f"recommends a cross-sell."
        )

    else:

        return (
            f"This customer shows very high incremental potential "
            f"with an estimated uplift of {uplift * 100:.1f}%. "
            f"Their historical discount response is "
            f"{discount_response * 100:.0f}%, making a personalized "
            f"offer a potentially valuable intervention."
        )

def calculate_discount_avoided(row):
    """
    Estimate promotional budget avoided when IncrementAI
    recommends not intervening with a customer.
    """

    if row["recommended_action"] == "No Action":
        return round(row["avg_order_value"] * 0.10, 2)

    return 0.0