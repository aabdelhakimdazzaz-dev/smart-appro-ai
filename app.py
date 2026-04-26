import streamlit as st

st.set_page_config(page_title="Smart Appro AI", layout="wide")
st.title("🚚 Smart Appro AI - PFE 2025")
st.success("✅ Deploy Naja7 f Python 3.14!")

st.header("📊 KPI Retards Fournisseurs")
c1, c2, c3 = st.columns(3)
c1.metric("Commandes à Risque Élevé", "2 🔴")
c2.metric("Perte Potentielle Évitable", "45,000 MAD") 
c3.metric("Accuracy Modèle IA", "91.3%")

st.header("📋 Données Exemple")
data = [
    {"ID_Cmd": 45001, "Fournisseur": "F102", "Pays": "Chine", "Risque_%": 87},
    {"ID_Cmd": 45003, "Fournisseur": "F203", "Pays": "Turquie", "Risque_%": 65},
    {"ID_Cmd": 45006, "Fournisseur": "F405", "Pays": "Italie", "Risque_%": 45}
]
st.table(data)

st.info("Version 0.2: Streamlit 1.39 + Protobuf 5.28 khdamin. Nzido Pandas mn ba3d.")
