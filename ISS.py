import requests
import time

print("🛰️ RADAR ACTIVÉ : Traque de l'ISS en continu...")
print("⚠️ Appuie sur Ctrl+C dans le terminal pour arrêter le radar.\n")
time.sleep(2)

# La boucle infinie : tout ce qui est décalé vers la droite va se répéter à l'infini
while True:
    
    # 1. On récupère les données
    url = "http://api.open-notify.org/iss-now.json"
    reponse = requests.get(url)
    donnees = reponse.json()

    # 2. On isole la géographie
    lat = donnees['iss_position']['latitude']
    lon = donnees['iss_position']['longitude']

    # 3. Le VRAI lien Google Maps qui marche à 100%
    lien_maps = f"https://www.google.com/maps?q={lat},{lon}"

    # 4. L'affichage radar
    print(f"📍 Cible en mouvement -> Lat: {lat} | Lon: {lon}")
    print(f"🗺️ Carte : {lien_maps}")
    print("-" * 50)

    # 5. CRUCIAL : On met le radar en pause 5 secondes. 
    # Sinon, on attaque le serveur spatial 1000 fois par seconde et il va nous bloquer !
    time.sleep(5)