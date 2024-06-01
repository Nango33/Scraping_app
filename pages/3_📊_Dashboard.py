import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
def dashboard():
    data_voitures = pd.read_csv('data/Expat_voitures_clean.csv')
    data_motos = pd.read_csv('data/Expat_moto_clean.csv')
    data_equipements = pd.read_csv('data/Expat_equipments_clean.csv')

    tabVoiture, tabMoto, tabEquipements = st.tabs(["Dashboard Voitures Expat", "Dashboard Motos Expat", "Dashboard Equipements Expat"])

    with tabVoiture :
        chart_type = st.radio("Choissez un type de graphe:", ("bar_plot", "scatter_plot","pie_chart"))
        if chart_type == "bar_plot":
            with st.container():
                fig = px.bar(data_voitures, x="etat", color="etat", title="Les voitures les plus vendues selon leur état")
                fig.show()
                st.plotly_chart(fig,use_container_width=True)
                with st.container():
                    fig = px.bar(data_voitures, x = "marque", color = 'marque', title="les voiture les plus vendues selon la marque")
                    fig.show()
                    st.plotly_chart(fig,use_container_width=True)

        elif chart_type == "scatter_plot":
            fig = px.scatter(data_voitures, x = 'année', y = 'prix(FCFA)', color='etat')
            st.plotly_chart(fig)
        
        elif chart_type == "pie_chart":
            bcount = data_voitures['boite vitesse'].value_counts().reset_index()
            fig = px.pie(bcount, values='boite vitesse', names= bcount.index, color='boite vitesse')
            st.plotly_chart(fig)

    
    with tabMoto:
        st.subheader("Quantité de motos disponibles selon leur état")
        fig = px.bar(data_motos, x="etat", color="etat")
        fig.show()
        st.plotly_chart(fig)

    with tabEquipements:
        st.dataframe(data_equipements)

st.set_page_config(page_title="Dashboard", page_icon="📊")
st.markdown("# Dashboard")
st.sidebar.header("Dashboard")

st.write(
    """Cette page montre different diagrammes basees sur les donnees scrapees et nettoyees avec Web Scraper"""
)

dashboard()