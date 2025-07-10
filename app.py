
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the labeled CSV
df = pd.read_csv("toxic_comments_labeled.csv")

# Title
st.title("🧠 Toxic Comment Detection Dashboard")

# Summary Stats
st.subheader("📊 Toxicity Summary")
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Comments", len(df))
    st.metric("Toxic Comments", df['is_toxic'].sum())
with col2:
    st.metric("Non-toxic Comments", len(df) - df['is_toxic'].sum())

# Pie Chart - Toxic vs Non-Toxic
st.subheader("⚖️ Toxic vs Non-Toxic Distribution")
tox_counts = df['is_toxic'].value_counts()
labels = ['Non-toxic', 'Toxic'] if False in tox_counts.index else ['Toxic']
fig, ax = plt.subplots()
ax.pie(tox_counts, labels=labels, autopct='%1.1f%%', startangle=140)
ax.axis('equal')
st.pyplot(fig)

# Bar Chart - Average Toxicity Scores per Category
st.subheader("📌 Average Toxicity Scores")
toxicity_labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
st.bar_chart(df[toxicity_labels].mean())

# Live-style Feed Display
st.subheader("💬 Comment Feed (Flagged)")
for _, row in df.iterrows():
    tag = "🔴" if row['is_toxic'] else "🟢"
    st.markdown(f"{tag} **{row['comment']}**")

# Optional: Filter Only Toxic
st.subheader("🔍 View Toxic Comments Only")
if st.checkbox("Show toxic comments only"):
    st.dataframe(df[df['is_toxic'] == True][['comment'] + toxicity_labels])