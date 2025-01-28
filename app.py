import streamlit as st

# Title
st.title("AI-Driven Firm Growth Simulation")

# Instructions
st.write("Allocate your $50M AI budget across the three options. The total must sum to $50M.")

# Inputs with validation
st.header("Allocate Your AI Budget ($50M)")

# Initialize session state to store allocations
if 'allocations' not in st.session_state:
    st.session_state.allocations = {'operational_efficiency': 30, 'product_innovation': 10, 'customer_insights': 10}

# Function to validate allocations
def validate_allocations(oe, pi, ci):
    total = oe + pi + ci
    if total != 50:
        st.error(f"Total allocations must sum to $50M. Current total: ${total}M")
        return False
    return True

# Sliders for allocations
operational_efficiency = st.slider(
    "Operational Efficiency", 
    0, 50, st.session_state.allocations['operational_efficiency'],
    key='oe'
)
product_innovation = st.slider(
    "Product Innovation", 
    0, 50, st.session_state.allocations['product_innovation'],
    key='pi'
)
customer_insights = st.slider(
    "Customer Insights", 
    0, 50, st.session_state.allocations['customer_insights'],
    key='ci'
)

# Submit button
if st.button("Submit"):
    if validate_allocations(operational_efficiency, product_innovation, customer_insights):
        # Store allocations in session state
        st.session_state.allocations = {
            'operational_efficiency': operational_efficiency,
            'product_innovation': product_innovation,
            'customer_insights': customer_insights
        }

        # Calculate Outcomes
        revenue_growth = (operational_efficiency * 0.15) + (product_innovation * 0.03) + (customer_insights * 0.05)
        market_share_growth = (product_innovation * 0.03) + (customer_insights * 0.02)
        workforce_reduction = operational_efficiency * 0.01

        # Display Results
        st.header("Simulation Results")
        st.write(f"Revenue Growth: {revenue_growth:.2f}%")
        st.write(f"Market Share Growth: {market_share_growth:.2f}%")
        st.write(f"Workforce Reduction: {workforce_reduction:.2f}%")
