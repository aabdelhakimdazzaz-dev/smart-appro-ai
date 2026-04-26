import streamlit as st

st.set_page_config(page_title="Smart Appro AI", layout="wide")
st.title("🚚 Smart Appro AI - PFE 2025")
st.success("✅ Deploy Naja7 bla Pillow!")

st.header("📊 KPI")
c1, c2, c3 = st.columns(3)
c1.metric("Commandes Risque", "2 🔴")
c2.metric("Perte Potentielle", "45,000 MAD") 
c3.metric("Accuracy IA", "91.3%")

st.header("📋 Data")
st.write({
    'ID_Cmd': [45001, 45003], 
    'Fournisseur': ['F102', 'F203'], 
    'Risque_%': [87, 65]
})

st.info("Version 0.1: Base khdama. Nzado pandas mn ba3d.")
