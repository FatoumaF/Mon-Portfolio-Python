from pathlib import Path
import streamlit as st
from PIL import Image

# Path parameters
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Professional CV Resume (3).pdf"
profil_pic_path = current_dir / "assets" / "profile-pic 2.png"

# General variables
PAGE_TITLE = "Portfolio Fatouma Fofana"
PAGE_ICON = ":wave:"
NAME = "Fatouma Fofana"
DESCRIPTION = (
    "Bonjour ! Je m’appelle Fatouma Fofana, développeuse Web junior en reconversion.\n\n"
    "Avant de me lancer dans le développement web, j’ai travaillé plusieurs années comme chargée de clientèle dans le domaine environnemental et technique. "
    "Cette expérience m’a permis d'acquérir des compétences précieuses telles que l’organisation, l’écoute, le conseil et de solides qualités relationnelles.\n\n"
    "Je n'ai pas toujours été passionnée par l'informatique, mais j'ai pris conscience de son impact crucial sur notre monde. "
    "C'est cette prise de conscience qui m'a poussée à m'aventurer dans ce domaine fascinant. "
    "Me voilà aujourd'hui au début de mon parcours, plongée dans mes premiers projets, confrontée à mes premiers bugs, "
    "je suis en train d'apprendre à aimer ce métier ce qui m'aide à évoluer chaque jour.\n\n"
    "Si vous cherchez quelqu'un de motivée, prête à s’épanouir dans le monde de la tech, je serais ravie d'en discuter autour d'un café. ☕"
)
EMAIL = "fatoumafofana24@gmail.com"
ADRESS="Paris 75010"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/fatouma-fofana-342808222/",
    "GitHub": "https://github.com/FatoumaF"
}

PROJECTS = {
    "🎮 JEU VIDEO": "https://www.lexaloffle.com/bbs/?tid=53272",
    "🔌 EXTENSION API": "https://github.com/FatoumaF/DatavizAPI",
    "📝 BLOG PHP": "https://github.com/FatoumaF/reseau-social-php-reseau_social_fatouma",
    "🛋️ SITES DE MEUBLE": "https://github.com/FatoumaF/projet-collectif-plateforme-de-vente-de-meubles-meuh-ble-1",
    "📚 BLOG LARAVEL": "https://github.com/FatoumaF/projet-collectif-microblogging-fatouma",
    "📱 Application mobile": "https://github.com/adatechschool/projet-mobile-front-eda-fatouma-aisseta"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load CSS, PDF & profile pic
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profil_pic_path)

# Hero section
col1, col2 = st.columns([1, 2], gap="medium")  # Adjust the ratio as needed

with col1:
    st.image(profile_pic, width=200)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Télécharger le CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(":email:", EMAIL)
    #st.write("adress", ADRESS)

# Social links
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# Utilisation de st.markdown pour formater le texte avec Markdown
st.write("# 🛠️ Qualifications")

# Utilisation de st.markdown pour formater chaque élément de manière plus lisible
st.markdown("""
- ✔️ **Concepteur Développeur d'Application TITRE RNCP 6 (BAC +3)**  
  *ADA TECH SCHOOL, En cours*

- ✔️ **BTS Commerce International (BAC +2)**  
  *PROGRESSCOM (CANDIDAT LIBRE) 2020*

- ✔️ **Baccalauréat Commerce**  
  *LYCÉE PIERRE LESCOT 2016*

""")
st.write("---")
# Header
st.title("Hard Skills")

# Subheader
st.subheader("💻 Hard Skills")

# HTML/CSS/JavaScript
st.write("### Frontend - 👩‍💻")
st.write("HTML/CSS/JavaScript")

# Python/PHP/Symfony
st.write("### Backend - 👩‍💻")
st.write("Python/PHP/POO(Symfony)")
st.write("Node.js(Express)")

st.write("### Base de donnée SQL🗄️ ")
st.write("Mysql(Phpmyadmin)/ Postgresql(Pgadmin)")

st.write("### Base de donnée no SQL 📚")
st.write("MONGO DB")

st.write("Api Rest/ Postman/ Jest/PHPunit")

# Add more skills with emojis and text here

# Soft Skills
# Header
st.write('#')
st.subheader("🤝 Soft Skills")

# Soft Skills list
soft_skills = [
    "Autonomie",
    "Travail en équipe",
    "Curiosité",
    "Méthode agile scrum"
]

# Display soft skills list
for skill in soft_skills:
    st.write("- " + skill)

# Mes projets
st.write('#')
st.subheader("📁 Mes projets")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# Work history
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "CHARGÉE DE CLIENTÈLE QUALIT'ENR/COMDATA CRM")
st.write("2019 – 2022")
st.write(
    """
- ► Gestion de la relation client
- ► Gestion des litiges et prise des rendez-vous
- ► Ouverture et gestion des dossiers dans les énergies renouvelables Gestion des audits
- ► Délivrance de certificat de qualité
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "COORDINATRICE LOGISTIQUE NEW EAST GENERAL TRADING DUBAI CHERIFS LOGISTICS, DUBAI")
st.write("2018-2019")
st.write(
    """
- ► Respect cahier des charges
- ► Vérifications des incoterms et dispatche des couts Cotations et calculs des coûts
- ► Travail au sein d’un groupe international
"""
)
