import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Approvisionnement AI", page_icon="🧠", layout="wide")

st.title("🧠 Smart Approvisionnement AI")
st.subheader("Système intelligent pour la gestion des stocks")

st.success("✅ Application déployée avec succès sur Hugging Face!")

col1, col2, col3 = st.columns(3)
col1.metric("📦 Produits", "1,234", "12%")
col2.metric("⚠️ Stock Faible", "56", "-8%")
col3.metric("🚚 Commandes", "89", "23%")

df = pd.DataFrame({
    'Mois': ['Jan', 'Fév', 'Mar', 'Avr', 'Mai'],
    'Ventes': [120, 135, 98, 145, 160],
    'Stock': [300, 280, 320, 290, 310]
})

fig = px.line(df, x='Mois', y=['Ventes', 'Stock'], title='Évolution Ventes vs Stock')
st.plotly_chart(fig, use_container_width=True)

st.info("👨‍🎓 Projet de Fin d'Études - Développé par Abdelhakim Dazzaz")
