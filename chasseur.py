import requests
import pyttsx3
import time
import csv

# --- TES PARAMÈTRES PERSONNELS ---
prenom = "Mosiah"
nom = "Estarque Nouguier"
mot_cle = "data" 
# ---------------------------------

print("\n" + "🎯"*3)
print(f"BOT RH V4 (SNIPER + HACKER) ACTIVÉ POUR {prenom.upper()} {nom.upper()}")
print(f"Recherche des meilleures offres Tech pour la FRANCE...")
print("🎯"*3 + "\n")
time.sleep(1)

# 1. On interroge les serveurs
url = f"https://remotive.com/api/remote-jobs?search={mot_cle}"
reponse = requests.get(url)
donnees = reponse.json()
offres = donnees.get('jobs', [])

# 2. Le Filtre France/Europe
offres_france = []
for job in offres:
    localisation = job.get('candidate_required_location', '').lower()
    if 'france' in localisation or 'europe' in localisation or 'anywhere' in localisation or 'worldwide' in localisation:
        offres_france.append(job)

nombre_trouve = len(offres_france)

if nombre_trouve > 0:
    nom_fichier = "Mes_Offres_Hacker.csv"
    
    # --- LE BOUCLIER ANTI-POSTES NULS (Le filtre Sniper) ---
    # Le script ne gardera l'offre QUE si le titre contient un de ces mots.
    mots_valides = ["data", "python", "analyst", "engineer", "developer", "ai", "machine learning", "junior", "intern"]
    # -------------------------------------------------------

    with open(nom_fichier, mode='w', newline='', encoding='utf-8-sig') as fichier_csv:
        colonnes = ['Entreprise', 'Poste', 'Localisation_Requise', 'Lien', 'Lettre de Motivation prête']
        writer = csv.DictWriter(fichier_csv, fieldnames=colonnes, delimiter=';')
        writer.writeheader()
        
        offres_sauvegardees = 0
        
        for job in offres_france:
            titre = job.get('title')
            entreprise = job.get('company_name')
            lien = job.get('url')
            loc = job.get('candidate_required_location')
            
            # Le Test Sniper
            titre_minuscule = titre.lower()
            poste_interessant = False
            for mot in mots_valides:
                if mot in titre_minuscule:
                    poste_interessant = True
                    break
            
            # Si le poste n'a pas un de nos mots-clés (ex: Office Assistant), on le jette !
            if not poste_interessant:
                continue
            
            # --- LA LETTRE DU HACKER (Spécial Junior Débrouillard) ---
            lettre = f"""Objet : Candidature au poste de {titre} - Un profil atypique et passionné

Madame, Monsieur,

Je ne vais pas vous faire une lettre classique. Je suis un développeur junior passionné par la data et l'automatisation. Pour vous prouver mes compétences techniques et ma motivation, sachez que j'ai moi-même codé le script Python qui a scanné le marché mondial ce matin, identifié votre offre de {titre} chez {entreprise} comme étant la plus pertinente, et généré cette candidature.

Bien que je sois au début de mon parcours académique en mathématiques et informatique, je n'attends pas qu'on me donne des cours pour apprendre. Je suis un profil atypique, capable d'apprendre de nouvelles technologies à une vitesse fulgurante, d'automatiser des processus fastidieux et de manipuler de la donnée. 

Je cherche une entreprise qui saura donner sa chance à un profil débrouillard, autonome et ultra-motivé pour du télétravail. 

Je serais ravi de vous montrer de quoi je suis capable lors d'un entretien.

Bien à vous,

{prenom} {nom}
(Développeur & Automatiseur)"""
            # ---------------------------------------------------------
            
            # On range les infos
            writer.writerow({
                'Entreprise': entreprise,
                'Poste': titre,
                'Localisation_Requise': loc,
                'Lien': lien,
                'Lettre de Motivation prête': lettre
            })
            print(f"✅ Vrai Poste Tech trouvé : {titre} chez {entreprise}")
            offres_sauvegardees += 1
            
            # On s'arrête dès qu'on a 10 offres parfaites
            if offres_sauvegardees >= 10:
                break

    print("\n" + "="*60)
    print(f"🎉 OPÉRATION TERMINÉE : {offres_sauvegardees} offres 100% TECH exportées !")
    print(f"Fichier créé : {nom_fichier}")
    print("="*60 + "\n")
    
    # Jarvis
    moteur = pyttsx3.init()
    moteur.setProperty('rate', 170)
    moteur.say(f"Mosiah, le nettoyage est terminé. J'ai gardé uniquement les vraies offres tech. Le fichier est prêt sur votre ordinateur.")
    moteur.runAndWait()
    del moteur

else:
    print(f"❌ Aucune offre compatible avec la France trouvée pour '{mot_cle}' à cette heure-ci.")