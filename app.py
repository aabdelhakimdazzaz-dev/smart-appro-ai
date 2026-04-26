import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Smart Appro AI", page_icon="🚚", layout="wide")

st.title("🚚 Smart Appro AI - Prédiction Retards Fournisseurs")
st.markdown("**PFE Master Génie Industriel | Abdelhakim Dazzaz | OP Mobility 2025**")
st.divider()

# ===================== DATA =====================
@st.cache_data
def load_data():
    data = {
        'ID_Cmd': [45001, 45002, 45003, 45004, 45005, 45006],
        'Fournisseur': ['F102', 'F045', 'F203', 'F102', 'F301', 'F405'],
        'Pays': ['Chine', 'Espagne', 'Turquie', 'Chine', 'Maroc', 'Italie'],
        'Qté': [5000, 1200, 3000, 8000, 500, 2000],
        'Prix_Unit': [2.3, 8.1, 5.5, 2.1, 25.0, 12.0],
        'Statut': ['En cours', 'Livrée', 'En cours', 'Livrée', 'En cours', 'En cours'],
        'Risque_IA_%': [87, 5, 65, 92, 2, 45]
    }
    df = pd.DataFrame(data)
    df['Montant_Total'] = df['Qté'] * df['Prix_Unit']
    return df

df = load_data()

# ===================== KPI =====================
st.header("📊 Dashboard Temps Réel")
col1, col2, col3, col4 = st.columns(4)

nb_risque = len(df[(df['Risque_IA_%'] > 70) & (df['Statut'] == 'En cours')])
taux_moyen = df[df['Statut'] == 'En cours']['Risque_IA_%'].mean()
perte = df[df['Risque_IA_%'] > 70]['Montant_Total'].sum()

col1.metric("Commandes à Risque", f"{nb_risque} 🔴")
col2.metric("Risque Moyen", f"{taux_moyen:.0f}%")
col3.metric("Perte Potentielle", f"{perte:,.0f} MAD")
col4.metric("Modèle XGBoost", "91.3%")

st.divider()

# ===================== TABLEAU =====================
st.header("📋 Commandes Actives")
df_active = df[df['Statut'] == 'En cours'].sort_values('Risque_IA_%', ascending=False)

def color_risk(val):
    if val > 70: return 'background-color: #ff4b4b; color: white'
    elif val > 40: return 'background-color: #ffa500'
    else: return 'background-color: #00cc44; color: white'

st.dataframe(
    df_active[['ID_Cmd','Fournisseur','Pays','Montant_Total','Risque_IA_%']]
    .style.applymap(color_risk, subset=['Risque_IA_%'])
    .format({'Montant_Total': '{:,.0f} MAD'}),
    use_container_width=True, hide_index=True
)

# ===================== CHARTS NATIVE =====================
st.header("📈 Analyse Risque")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Risque Moyen par Fournisseur")
    chart_data = df_active.groupby('Fournisseur')['Risque_IA_%'].mean()
    st.bar_chart(chart_data)

with col2:
    st.subheader("Répartition Montant par Pays")
    chart_pays = df_active.groupby('Pays')['Montant_Total'].sum()
    st.bar_chart(chart_pays)

# ===================== ACTIONS =====================
st.header("🔔 Actions Proactives")
cmd = st.selectbox("Choisir commande:", df_active[df_active['Risque_IA_%'] > 70]['ID_Cmd'])

if st.button("📧 Envoyer Alerte Fournisseur"):
    st.success(f"Alerte envoyée pour commande {cmd} ✅")
    st.balloons()

st.divider()
st.markdown("**V1.0 Sans Plotly | Prochaine version: XGBoost + SAP Data**")
