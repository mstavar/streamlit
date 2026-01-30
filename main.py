import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import mysql.connector

st.set_page_config(
    page_title="Monthly Finance",
    layout="wide"
)

# --- DB CONNECTION ---
@st.cache_data(ttl=600)
def load_data():
    conn = mysql.connector.connect(
        host=st.secrets["DB_HOST"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASS"],
        database=st.secrets["DB_NAME"]
    )

    query = """
        SELECT 
            month AS Month,
            vanzari AS Vanzari,
            achizitii AS Achizitii,
            profit AS Profit
        FROM monthly_finance
        ORDER BY id
    """

    df = pd.read_sql(query, conn)
    conn.close()
    return df


df = load_data()

# --- PLOT ---
fig = px.bar(
    df,
    x='Month',
    y=['Vanzari', 'Achizitii'],
    barmode='group',
    title="Situație financiară lunară"
)

fig.add_scatter(
    x=df['Month'],
    y=df['Profit'],
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
    legend=dict(x=1.05, y=1)
)

st.plotly_chart(fig, use_container_width=True)
