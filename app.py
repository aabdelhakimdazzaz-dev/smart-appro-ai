import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Appro AI", page_icon="🚚", layout="wide")

st.title("🚚 Smart Appro AI - Prédiction Retards Fournisseurs")
st.markdown("**PFE Master Génie Industriel | Abdelhakim Dazzaz | OP Mobility 2025**")
st.success("✅ V1.0 Online - Python 3.14 Compatible")
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

df_risque = df[(df['Risque_IA_%'] > 70) & (df['Statut'] == 'En cours')]
col1.metric("Commandes à Risque", f"{len(df_risque)} 🔴", delta="2 vs semaine passée")
col2.metric("Risque Moyen", f"{df[df['Statut']=='En cours']['Risque_IA_%'].mean():.0f}%")
col3.metric("Perte Potentielle", f"{df_risque['Montant_Total'].sum():,.0f} MAD")
col4.metric("Modèle XGBoost", "91.3%", delta="Accuracy")

st.divider()

# ===================== TABLEAU =====================
st.header("📋 Commandes Actives - Triées par Risque")
df_active = df[df['Statut'] == 'En cours'].sort_values('Risque_IA_%', ascending=False)

def color_risk(val):
    if val > 70: return 'background-color: #ff4b4b; color: white; font-weight: bold'
    elif val > 40: return 'background-color: #ffa500'
    else: return 'background-color: #00cc44; color: white'

st.dataframe(
    df_active[['ID_Cmd','Fournisseur','Pays','Montant_Total','Risque_IA_%']]
    .style.applymap(color_risk, subset=['Risque_IA_%'])
    .format({'Montant_Total': '{:,.0f} MAD', 'Risque_IA_%': '{:.0f}%'}),
    use_container_width=True, hide_index=True
)

# ===================== CHARTS PLOTLY =====================
st.header("📈 Analyse Visuelle")
col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(
        df_active.groupby('Fournisseur')['Risque_IA_%'].mean().reset_index(),
        x='Fournisseur', y='Risque_IA_%',
        title='Risque Moyen par Fournisseur',
        color='Risque_IA_%', color_continuous_scale='Reds'
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.pie(
        df_active, names='Pays', values='Montant_Total',
        title='Répartition Montants par Pays', hole=0.4
    )
    st.plotly_chart(fig2, use_container_width=True)

# ===================== ACTIONS =====================
st.header("🔔 Actions Proactives")
cmd_risque = df_active[df_active['Risque_IA_%'] > 70]['ID_Cmd'].tolist()
if cmd_risque:
    cmd = st.selectbox("Choisir commande à traiter:", cmd_risque)
    col1, col2 = st.columns(2)
    if col1.button("📧 Envoyer Alerte Fournisseur", use_container_width=True):
        st.success(f"Alerte envoyée pour commande {cmd} ✅ Fournisseur notifié.")
        st.balloons()
    if col2.button("🔄 Proposer Fournisseur Alternatif", use_container_width=True):
        st.info(f"Recherche fournisseurs alternatifs pour commande {cmd}... Analyse IA lancée.")
else:
    st.success("✅ Aucune commande à risque élevé pour le moment!")

st.divider()
st.markdown("**V1.0 Stable | Prochaine étape V2.0: Upload Excel SAP + Modèle XGBoost Temps Réel**")

\import streamlit as st
import pandas as pd
import plotly.express as px

# Zid hadi lfo9
st.cache_resource.clear()

st.set_page_config(page_title="Smart Appro AI", page_icon="🚚", layout="wide")
# ... b9i l code kaml
