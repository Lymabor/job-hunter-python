import streamlit as st
import requests
import pandas as pd

# 1. Configuration de la page
st.set_page_config(page_title="Mosiah Job Hunter", page_icon="🎯")

st.title("🎯 Mosiah Job Hunter - V1.0")
st.markdown("### L'outil qui hacke le marché du travail en télétravail")

# 2. Sidebar pour tes infos
st.sidebar.header("Paramètres")
prenom = st.sidebar.text_input("Prénom", "Mosiah")
nom = st.sidebar.text_input("Nom", "Estarque Nouguier")
mot_cle = st.sidebar.text_input("Poste recherché", "data")

# 3. Le bouton magique
if st.button("🚀 Lancer le radar"):
    st.write(f"Recherche en cours pour : **{mot_cle}**...")
    
    url = f"https://remotive.com/api/remote-jobs?search={mot_cle}"
    try:
        reponse = requests.get(url)
        donnees = reponse.json()
        offres = donnees.get('jobs', [])
        
        mots_valides = ["data", "python", "analyst", "engineer", "developer", "ai", "machine learning", "junior", "intern"]
        resultats = []

        for job in offres:
            loc = job.get('candidate_required_location', '').lower()
            titre = job.get('title')
            
            if any(x in loc for x in ['france', 'europe', 'anywhere', 'worldwide']):
                if any(m in titre.lower() for m in mots_valides):
                    resultats.append({
                        "Entreprise": job.get('company_name'),
                        "Poste": titre,
                        "Localisation": job.get('candidate_required_location'),
                        "Lien": job.get('url')
                    })
        
        if resultats:
            st.success(f"BINGO ! {len(resultats)} offres tech trouvées.")
            df = pd.DataFrame(resultats)
            st.dataframe(df)
            
            st.markdown("---")
            st.subheader("📝 Ta lettre de motivation (Hacker Style)")
            top_job = resultats[0]
            lettre = f"""
            **Objet : Candidature au poste de {top_job['Poste']}**
            
            Madame, Monsieur,
            
            Je ne vais pas vous faire une lettre classique. Je suis un développeur junior passionné par la data et l'automatisation. Sachez que j'ai moi-même codé l'application qui a scanné le marché mondial ce matin, identifié votre offre chez {top_job['Entreprise']} et généré cette candidature.
            
            Je cherche une entreprise qui saura donner sa chance à un profil débrouillard et autonome.
            
            Cordialement,  
            **{prenom} {nom}**
            """
            st.info(lettre)
            
        else:
            st.warning("Aucune offre trouvée. Essaie un autre mot-clé !")
            
    except Exception as e:
        st.error(f"Erreur de connexion : {e}")