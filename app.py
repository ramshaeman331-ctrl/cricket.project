import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Cricket Dashboard", layout="wide")
st.title("🏏 Cricket Performance Analysis Dashboard")
st.markdown("---")

# Dummy data generator
np.random.seed(42)
dates = pd.date_range(start="2021-01-01", periods=100, freq="D")
teams = ["Pakistan", "India", "Australia", "England", "South Africa"]
df = pd.DataFrame({
    'Date': np.random.choice(dates, 100),
    'Team': np.random.choice(teams, 100),
    'Runs': np.random.randint(0, 120, 100),
    'Wickets': np.random.randint(0, 5, 100),
    'Season': np.random.choice(["2021", "2022", "2023", "2024"], 100)
})

st.sidebar.header("🛠️ Filters")
selected_team = st.sidebar.selectbox("Select Team", teams)
df_filtered = df[df['Team'] == selected_team]

col1, col2 = st.columns(2)
with col1:
    st.subheader("Runs Distribution")
    fig, ax = plt.subplots()
    df_filtered['Runs'].plot(kind='hist', bins=10, color='green', ax=ax)
    st.pyplot(fig)
with col2:
    st.subheader("Wickets Breakdown")
    fig, ax = plt.subplots()
    df_filtered['Wickets'].value_counts().plot(kind='bar', color='skyblue', ax=ax)
    st.pyplot(fig)
