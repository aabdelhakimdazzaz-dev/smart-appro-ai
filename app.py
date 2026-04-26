import streamlit as st

st.set_page_config(page_title="Smart Appro AI", layout="wide")
st.title("🚚 Smart Appro AI - PFE 2025")
st.success("✅ Deploy Naja7! Version 0.1")

st.header("📊 KPI Retards Fournisseurs")
c1, c2, c3 = st.columns(3)
c1.metric("Commandes à Risque Élevé", "2 🔴")
c2.metric("Perte Potentielle Évitable", "45,000 MAD") 
c3.metric("Accuracy Modèle IA", "91.3%")

st.header("📋 Données Exemple")
st.write({
    'ID_Cmd': [45001, 45003, 45006],
    'Fournisseur': ['F102', 'F203', 'F405'],
    'Pays': ['Chine', 'Turquie', 'Italie'],
    'Risque_IA_%': [87, 65, 45]
})

st.info("Version 0.1: Test Deploy Réussi")
