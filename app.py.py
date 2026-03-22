import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="AI Capital Allocation Simulator", layout="wide")

st.title("💰 AI Capital Allocation Strategy Dashboard")
st.markdown("Decision Intelligence for Investment Optimization")

st.markdown("---")

# -----------------------------
# INPUT SECTION
# -----------------------------
col1, col2 = st.columns([1,3])

with col1:
    st.subheader("⚙️ Investment Strategy")

    total_budget = st.slider("Total Budget (₹ Cr)", 50, 500, 100)

    prod = st.slider("Production %", 0, 100, 30)
    mkt = st.slider("Marketing %", 0, 100, 25)
    rnd = st.slider("R&D %", 0, 100, 25)
    sc = st.slider("Supply Chain %", 0, 100, 20)

    total = prod + mkt + rnd + sc

    if total != 100:
        st.error("Total allocation must be 100%")

# -----------------------------
# SIMULATION FUNCTION
# -----------------------------
def simulate_strategy(prod, mkt, rnd, sc, total_budget):

    allocation = {
        "Production": prod/100,
        "Marketing": mkt/100,
        "R&D": rnd/100,
        "SupplyChain": sc/100
    }

    roi_models = {
        "Production": (0.12, 0.05),
        "Marketing": (0.15, 0.07),
        "R&D": (0.20, 0.15),
        "SupplyChain": (0.10, 0.03)
    }

    simulations = 1000
    results = []

    for _ in range(simulations):
        total_roi = 0

        for area in allocation:
            invest = total_budget * allocation[area]
            mean, risk = roi_models[area]

            # Monte Carlo Simulation
            roi = invest * np.random.normal(mean, risk)
            total_roi += roi

        results.append(total_roi)

    return results

# -----------------------------
# RUN SIMULATION
# -----------------------------
if total == 100:

    results = simulate_strategy(prod, mkt, rnd, sc, total_budget)

    avg_return = np.mean(results)
    risk = np.std(results)
    best_case = max(results)
    worst_case = min(results)

    # -----------------------------
    # KPI DISPLAY
    # -----------------------------
    with col2:
        st.subheader("📊 Executive Summary")

        k1, k2, k3, k4 = st.columns(4)

        k1.metric("Expected ROI (₹ Cr)", round(avg_return,2))
        k2.metric("Risk (Std Dev)", round(risk,2))
        k3.metric("Best Case (₹ Cr)", round(best_case,2))
        k4.metric("Worst Case (₹ Cr)", round(worst_case,2))

    # -----------------------------
    # INSIGHT SECTION
    # -----------------------------
    st.markdown("---")
    st.subheader("🧠 Strategic Insight")

    if risk > 15:
        st.warning("High Risk Strategy – Heavy exposure to volatile areas like R&D")
    elif avg_return > 18:
        st.success("High Growth Strategy – Strong return potential")
    else:
        st.info("Balanced Strategy – Moderate return with controlled risk")

    # -----------------------------
    # VISUALIZATION
    # -----------------------------
    st.subheader("📈 ROI Distribution (Simulation)")

    fig, ax = plt.subplots()
    ax.hist(results, bins=30)
    ax.set_xlabel("Return (₹ Cr)")
    ax.set_ylabel("Frequency")

    st.pyplot(fig)
