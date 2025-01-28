import streamlit as st

# Title
st.title("AI-Driven Firm Growth Simulation")

# Inputs
st.header("Allocate Your AI Budget ($50M)")
operational_efficiency = st.slider("Operational Efficiency", 0, 50, 30)
product_innovation = st.slider("Product Innovation", 0, 50, 10)
customer_insights = st.slider("Customer Insights", 0, 50, 10)

# Calculate Outcomes
revenue_growth = (operational_efficiency * 0.15) + (product_innovation * 0.03) + (customer_insights * 0.05)
market_share_growth = (product_innovation * 0.03) + (customer_insights * 0.02)
workforce_reduction = operational_efficiency * 0.01

# Display Results
st.header("Simulation Results")
st.write(f"Revenue Growth: {revenue_growth:.2f}%")
st.write(f"Market Share Growth: {market_share_growth:.2f}%")
st.write(f"Workforce Reduction: {workforce_reduction:.2f}%")
