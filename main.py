import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="Charts demo",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.header("Displaying Charts")
# Sample Data
data = {
    'Month': ["Ian","Feb","Mar","Apr","Mai","Iun","Iul","Aug","Sep","Oct","Nov","Dec"],
    'Bar1': [10000,12000,14000,13000,15000,16000,15500,17000,18000,17500,19000,21000],
    'Bar2': [7000,8000,8500,8200,9000,9500,9200,10000,10500,10200,11000,12000],
    'Line': [30,33,39,37,40,41,41,41,42,42,42,43]
}
df = pd.DataFrame(data)

# Create Plotly Figure
fig = go.Figure()

# Add Bar 1
fig.add_trace(go.Bar(x=df['Month'], y=df['Bar1'], name='Vanzari', marker_color='indianred'))

# Add Bar 2
fig.add_trace(go.Bar(x=df['Month'], y=df['Bar2'], name='Achizitii', marker_color='lightsalmon'))

# Add Line
fig.add_trace(go.Scatter(x=df['Month'], y=df['Line'], name='Profit', mode='lines+markers', line=dict(color='blue', width=3)))

# Update layout for combined appearance
fig.update_layout(
    title='Combined Bar and Line Chart',
    xaxis=dict(title='Month'),
    yaxis=dict(title='Values (lei)'),
    barmode='group' # Use 'overlay' or 'stack' for different effects
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)
