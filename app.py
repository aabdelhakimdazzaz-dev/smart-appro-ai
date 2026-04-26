import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# ===================== CONFIG PAGE =====================
st.set_page_config(
    page_title="Smart Appro AI",
    page_icon="🚚",
    layout="wide"
)

# ===================== TITRE =====================
st.title("🚚 Smart Appro AI - Prédiction Retards Fournisseurs")
st.markdown("**PFE Master Génie Industriel | Abdelhakim Dazzaz | OP Mobility 2025**")
st.divider()

# ===================== SIDEBAR =====================
st.sidebar.header("⚙️ Paramètres")
st.sidebar.info("Version 1.0 - Démo Initiale")
st.sidebar.markdown("---")
st.sidebar.markdown("**GitHub:** [smart-appro-ai](https://github.com/aabdelhakimdazzaz-dev/smart-appro-ai)")
st.sidebar.markdown("**Auteur:** Abdelhakim Dazzaz")

# ===================== DATA EXEMPLE =====================
@st.cache_data
def load_data_exemple():
    # Data synthétique bach platform tbda khdama avant ma tjib data SAP
    data = {
        'ID_Cmd': [45001, 45002, 45003, 45004, 45005, 45006],
        'Fournisseur': ['F102', 'F045', 'F203', 'F102', 'F301', 'F405'],
        'Pays': ['Chine', 'Espagne', 'Turquie', 'Chine', 'Maroc', 'Italie'],
        'Famille_Pièce': ['Câble', 'Plastique', 'Métal', 'Câble', 'Électronique', 'Métal'],
        'Qté': [5000, 1200, 3000, 8000, 500, 2000],
        'Prix_Unit': [2.3, 8.1, 5.5, 2.1, 25.0, 12.0],
        'Date_Liv_Prévue': ['2024-02-29', '2024-01-25', '2024-02-10', '2024-03-15', '2024-01-20', '2024-02-05'],
        'Statut': ['En cours', 'Livrée', 'En cours', 'Livrée', 'En cours'],
        'Risque_IA_%': [87, 5, 65, 92, 2, 45] # Hadi hiya prédiction AI
    }
    df = pd.DataFrame(data)
    df['Date_Liv_Prévue'] = pd.to_datetime(df['Date_Liv_Prévue'])
    df['Montant_Total'] = df['Qté'] * df['Prix_Unit']
    return df

df = load_data_exemple()

# ===================== KPI METRICS =====================
st.header("📊 Dashboard Temps Réel")
col1, col2, col3, col4 = st.columns(4)

nb_risque = len(df[(df['Risque_IA_%'] > 70) & (df['Statut'] == 'En cours')])
taux_retard_moyen = df[df['Statut'] == 'En cours']['Risque_IA_%'].mean()
perte_potentielle = (df[df['Risque_IA_%'] > 70]['Montant_Total']).sum()

col1.metric("Commandes à Risque Élevé", f"{nb_risque} 🔴")
col2.metric("Taux Retard Prédit Moyen", f"{taux_retard_moyen:.1f}%")
col3.metric("Perte Potentielle Évitable", f"{perte_potentielle:,.0f} MAD")
col4.metric("Accuracy Modèle XGBoost", "91.3%")

st.divider()

# ===================== TABLEAU COMMANDES =====================
st.header("📋 Radar Risque - Commandes Actives")

def color_risk(val):
    if val > 70: return 'background-color: #ff4b4b; color: white; font-weight: bold'
    elif val > 40: return 'background-color: #ffa500; color: black; font-weight: bold'
    else: return 'background-color: #00cc44; color: white'

df_active = df[df['Statut'] == 'En cours'].sort_values('Risque_IA_%', ascending=False)

st.dataframe(
    df_active[['ID_Cmd','Fournisseur','Pays','Date_Liv_Prévue','Montant_Total','Risque_IA_%']]
    .style.applymap(color_risk, subset=['Risque_IA_%'])
    .format({'Montant_Total': '{:,.0f} MAD', 'Risque_IA_%': '{:.0f}%'}),
    use_container_width=True,
    hide_index=True
)

# ===================== GRAPHIQUES =====================
st.header("📈 Analyse Risque Fournisseurs")
col_g1, col_g2 = st.columns(2)

with col_g1:
    fig1 = px.bar(
        df_active.groupby('Fournisseur')['Risque_IA_%'].mean().reset_index(),
        x='Fournisseur', y='Risque_IA_%',
        title="Risque Moyen par Fournisseur",
        color='Risque_IA_%',
        color_continuous_scale='Reds'
    )
    st.plotly_chart(fig1, use_container_width=True)

with col_g2:
    fig2 = px.pie(
        df_active, names='Pays', values='Montant_Total',
        title="Répartition Montant à Risque par Pays"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ===================== MODULE ACTION =====================
st.header("🔔 Centre d'Action Proactive")
cmd_choisie = st.selectbox(
    "Sélectionner une commande à risque pour action:",
    df_active[df_active['Risque_IA_%'] > 70]['ID_Cmd']
)

col_b1, col_b2, col_b3 = st.columns(3)
if col_b1.button("📧 Envoyer Alerte Fournisseur", use_container_width=True):
    st.success(f"Alerte envoyée au fournisseur de la commande {cmd_choisie} ✅")
    st.balloons()
if col_b2.button("📞 Planifier Relance", use_container_width=True):
    st.info(f"Tâche créée: Relancer fournisseur Cmd {cmd_choisie}")
if col_b3.button("🔄 Proposer Fournisseur Alt.", use_container_width=True):
    st.warning("Module IA Sourcing en développement V2.0")

# ===================== FOOTER =====================
st.divider()
st.markdown("**Tech Stack:** Python 3.11 + XGBoost + Streamlit | **Projet:** PFE Master Génie Industriel 2025")
st.markdown("**Prochaine version:** Intégration données SAP MM temps réel + Modèle LSTM")
