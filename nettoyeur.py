import os
import shutil
from pathlib import Path
import time

# 1. La cible : On trouve automatiquement ton dossier "Téléchargements"
dossier_cible = "E:/"

print("\n" + "="*50)
print(f"🧹 DÉMARRAGE DU NETTOYEUR SUR : {dossier_cible}")
print("="*50 + "\n")
time.sleep(1) # Petit suspense

# 2. Les règles de rangement : On crée nos "boîtes"
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents_Cours": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".csv"],
    "Logiciels_et_Zip": [".exe", ".msi", ".zip", ".rar", ".7z"],
    "Musiques_et_Videos": [".mp3", ".wav", ".mp4", ".avi", ".mkv"]
}

fichiers_ranges = 0

# 3. L'exécution : Le script fouille chaque fichier un par un
for fichier in os.listdir(dossier_cible):
    chemin_fichier = os.path.join(dossier_cible, fichier)
    
    # Sécurité : Si c'est déjà un dossier, on n'y touche pas
    if os.path.isdir(chemin_fichier):
        continue
        
    # On isole l'extension du fichier (ex: on garde juste ".pdf")
    _, extension = os.path.splitext(fichier)
    extension = extension.lower() # On met tout en minuscules pour éviter les bugs
    
    # 4. Le tri : On cherche dans quelle boîte le mettre
    for nom_boite, extensions_valides in categories.items():
        if extension in extensions_valides:
            
            # On crée la boîte (le dossier) si elle n'existe pas encore
            chemin_boite = os.path.join(dossier_cible, nom_boite)
            if not os.path.exists(chemin_boite):
                os.makedirs(chemin_boite)
            
            # L'action magique : On déplace le fichier !
            shutil.move(chemin_fichier, os.path.join(chemin_boite, fichier))
            print(f"✅ Rangé : {fichier} ---> [{nom_boite}]")
            fichiers_ranges += 1
            break # Le fichier est rangé, on passe au suivant

# 5. Le rapport final
print("\n" + "="*50)
print(f"✨ OPÉRATION TERMINÉE : {fichiers_ranges} fichiers triés à la vitesse de la lumière.")
print("="*50 + "\n")