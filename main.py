import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import requests

st.set_page_config(
    page_title="Monthly Finance",
    layout="wide"
)


@st.cache_data(ttl=600)
def load_data():
    url = "https://grafic.prosoftsrl.ro/api/monthly_finance.php?key=abc123XyZ!"
    return pd.read_json(url)

df = load_data()

# --- PLOT ---
fig = px.bar(
    df,
    x='month', 
    y=['Vânzări', 'Achiziții']
    barmode='group',
    title="Situație financiară lunară",
    labels={
        'month': 'Lună'
    }
)

fig.add_scatter(
    x=df['month'],name='Profrrit (%)',
    y=df['profit_percent'],
    name='Profit (%)',
    yaxis='y2',
    line=dict(color='red', width=3)
)

fig.update_layout(
    yaxis=dict(title='Valoare (lei)'),
    yaxis2=dict(
        title='Profit (%)',
        overlaying='y',
        side='right'
    ),
    legend_title_text="Indicatori",
    legend=dict(x=1.05, y=1)
)

st.plotly_chart(fig, use_container_width=True)
