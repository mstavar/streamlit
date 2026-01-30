import streamlit as st
import plotly.express as px
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
    'Vanzari': [10000,12000,14000,13000,15000,16000,15500,17000,18000,17500,19000,21000],
    'Achizitii': [7000,8000,8500,8200,9000,9500,9200,10000,10500,10200,11000,12000],
    'Profit': [30,33,39,37,40,41,41,41,42,42,42,43] # Scale is different
}


df = pd.DataFrame(data)

# Create base figure with bars
fig = px.bar(df, x='Month', y=['Vanzari', 'Achizitii'], barmode='group', title="Dual Axis Chart")

# Add line plot on secondary y-axis
fig.add_scatter(x=df['Month'], y=df['Profit'], name='Profit', yaxis='y2', line=dict(color='red', width=3))

# Update layout to add secondary Y-axis
fig.update_layout(
    yaxis=dict(title='Values (lei)'),
    yaxis2=dict(title='Values (%)', overlaying='y', side='right'),
    legend=dict(x=1.1, y=1)
)

# Display in Streamlit
st.plotly_chart(fig)
