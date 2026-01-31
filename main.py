import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import requests

st.set_page_config(
    page_title="Monthly Finance",
    layout="wide"
)

@st.cache_data(ttl=3600)
def get_years():
    url = "https://grafic.prosoftsrl.ro/api/available_years.php"
    return requests.get(url).json()

years = get_years()

selected_year = st.selectbox(
    "Selectează anul",
    years,
    index=0
)

@st.cache_data(ttl=600)
def load_data(year):
    url = f"https://grafic.prosoftsrl.ro/api/monthly_finance.php?year={year}&key=abc123XyZ!"
    return pd.read_json(url)

df = load_data(selected_year)
month_map = {
    1: "Ian", 2: "Feb", 3: "Mar", 4: "Apr",
    5: "Mai", 6: "Iun", 7: "Iul", 8: "Aug",
    9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}

df["Lună"] = df["month"].map(month_map)

# --- PLOT ---
fig = px.bar(
    df,
    x="Lună",
    y=["Vânzări", "Achiziții"],
    barmode="group",
    title=f"Situație financiară lunară – {selected_year}"
)


fig.add_scatter(
    x=df["Lună"],
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
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.12,
        xanchor="center",
        x=0.5
    )
)

st.plotly_chart(fig, use_container_width=True)
