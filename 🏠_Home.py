import requests
import streamlit as st
from streamlit_lottie import st_lottie
import leafmap.foliumap as leafmap



st.set_page_config(layout="wide")

# USE LOTTIE
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_maxj5quq.json")
# Customize the sidebar
markdown = """
Wu, Q. (2021). Leafmap: A Python package for interactive mapping and geospatial analysis with minimal coding in a Jupyter environment. Journal of Open Source Software, 6(63), 3414. https://doi.org/10.21105/joss.03414

"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("Présentation de Données Géospatiales")

st.markdown(
    """
    Bonjour et bienvenue sur ma page d'accueil ! Je suis analyste de données spatiales et cartographe, 
    et j'utilise les technologies les plus récentes pour présenter mes résultats de manière dynamique et interactive.
    Ma passion pour les données spatiales m'a conduit à développer des solutions innovantes en utilisant des outils tels que Streamlit et Leaflet. 
    Grâce à ces technologies, 
    je suis capable de créer des applications web interactives qui permettent à mes utilisateurs d'explorer mes cartes et mes données en temps réel.

    Mon objectif est de rendre mes données accessibles et compréhensibles pour tout le monde, grâce à une interface simple et intuitive.
    J'utilise des graphiques, des cartes et des visualisations pour illustrer mes résultats et faciliter leur interprétation.

    Je suis fier de contribuer à l'avancement de la science des données spatiales et de travailler sur des projets qui ont un impact réel sur notre environnement. 
    Si vous avez des questions ou des commentaires sur mon travail, n'hésitez pas à me contacter.
    """
)

st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template) or [use it as a template](https://github.com/giswqs/streamlit-multipage-template/generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)


st.header(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/redgisafrica@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" rows="10" placeholder="Your Message Here" required></textarea> 
    <button type="submit">Send</button> 
    
</form>
"""  



with st.container():
    left_column, right_column = st.columns(2)

with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)


with right_column:
    st_lottie(lottie_coding, key= None)  

   
        
    
            

