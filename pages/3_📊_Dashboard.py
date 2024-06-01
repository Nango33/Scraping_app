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
        #chart_type = st.radio("Choissez un type de graphe:", ("bar_plot", "scatter_plot","pie_chart"))
        #if chart_type == "bar_plot":
        with st.container():
            fig = px.bar(data_voitures, x="etat", color="etat", title="Les voitures les plus publiees selon leur état")
            st.plotly_chart(fig,use_container_width=True)

        with st.container():
            fig = px.bar(data_voitures, x = "marque", color = 'marque', title="les voiture les plus publiees selon la marque")
            st.plotly_chart(fig,use_container_width=True)

        with st.container():
            fig = px.scatter(data_voitures, x = 'année', y = 'prix(FCFA)', color='etat', title="Rapartition par prix et etat")
            st.plotly_chart(fig)

        # elif chart_type == "scatter_plot":
        #     fig = px.scatter(data_voitures, x = 'année', y = 'prix(FCFA)', color='etat')
        #     st.plotly_chart(fig)
        
        # elif chart_type == "pie_chart":
        #     bcount = data_voitures['boite vitesse'].value_counts().reset_index()
        #     fig = px.pie(bcount, values='boite vitesse', names= bcount.index, color='boite vitesse')
        #     st.plotly_chart(fig)

    
    with tabMoto:
        with st.container():
            fig = px.bar(data_motos, x="etat", color="etat", title="Les motos les plus publiees selon leur état")
            st.plotly_chart(fig,use_container_width=True)

        with st.container():
            fig = px.bar(data_motos, x = "marque", color = 'marque', title="les motos les plus publiees selon la marque")
            st.plotly_chart(fig,use_container_width=True)

        with st.container():
            fig = px.scatter(data_motos, x = 'année', y = 'prix', color='etat', title="Rapartition par prix et etat")
            st.plotly_chart(fig)

        
    with tabEquipements:
        with st.container():
            fig = px.bar(data_equipements, x="etat", color="etat", title="Les equipements les plus publies selon leur état")
            st.plotly_chart(fig,use_container_width=True)
        with st.container():
            fig = px.scatter(data_equipements, x = "etat", y = "prix", color = 'prix', title="Rapartition par prix et etat")
            st.plotly_chart(fig,use_container_width=True)

st.set_page_config(page_title="Dashboard", page_icon="📊")
st.markdown("# Dashboard")
st.sidebar.header("Dashboard")

st.write(
    """Cette page montre different diagrammes basees sur les donnees scrapees et nettoyees avec BSoup"""
)

dashboard()
