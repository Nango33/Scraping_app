import streamlit as st
import pandas as pd

st.set_page_config(page_title="Donnees venant de Web Scraper", page_icon="🧮")
st.markdown("# Web Scraper")
st.sidebar.header("Web Scraper")

st.markdown("Cette page montre differentes donnees non nettoyer scraper avec Web Scraper")
st.write("**Library utilisés:** pandas, streamlit")
st.write("**Sources des données:** [Expat-Dakar](https://www.expat-dakar.com/).")



def webScraperData():
    st.title('Données scrappées avec Web Scraper')

    data_voiture = pd.read_csv('data/Expat_voitures.csv')
    data_motos = pd.read_csv('data/Expat_moto.csv')
    data_equipements = pd.read_csv('data/Expat_equipements_pieces.csv')

    tabVoiture, tabMoto, TabEquipements = st.tabs(['Voitures Expat Dakar', 'Motos Expat Dakar', 'Equipements Expat Dakar'])
    tabVoiture.write('Voitures Expat Dakar')
    tabMoto.write('Motos Expat Dakar')
    TabEquipements.write('Equipements Expat Dakar')

    with tabVoiture:
        st.write('Data dimension: ' + str(data_voiture.shape[0]) + ' rows and ' + str(data_voiture.shape[1]) + ' columns.')
        st.dataframe(data_voiture, use_container_width=True)
        st.download_button(label="Download data as CSV",
                           data=data_voiture.to_csv().encode("utf-8"),
                           file_name="Expat_voitures.csv",
                           mime="text/csv")
        

    with tabMoto:
        st.write('Data dimension: ' + str(data_motos.shape[0]) + ' rows and ' + str(data_motos.shape[1]) + ' columns.')
        st.dataframe(data_motos, use_container_width=True)
        st.download_button(label="Download data as CSV",
                           data=data_motos.to_csv().encode("utf-8"),
                           file_name="Expat_motos.csv",
                           mime="text/csv")
        

    with TabEquipements:
        st.write('Data dimension: ' + str(data_equipements.shape[0]) + ' rows and ' + str(data_equipements.shape[1]) + ' columns.')
        st.dataframe(data_equipements, use_container_width=True)
        st.download_button(label="Download data as CSV",
                           data=data_equipements.to_csv().encode("utf-8"),
                           file_name="Expat_equipements.csv",
                           mime="text/csv")
        

webScraperData()


