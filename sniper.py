import requests
import time

# --- PARAMÈTRES DU SNIPER ---
cible = "bitcoin"
# On va fixer un prix de déclenchement (en euros). 
# Mets un chiffre très haut au début (ex: 1000000) juste pour être sûr que l'alarme sonne tout de suite et tester le code !
prix_declenchement = 1000000 

print("\n" + "🎯"*3)
print("SNIPER FINANCIER ACTIVÉ")
print(f"Cible verrouillée : {cible.upper()}")
print(f"Tir automatique programmé si le prix passe sous : {prix_declenchement} €")
print("🎯"*3 + "\n")
time.sleep(2)

# Le radar tourne en boucle
while True:
    try:
        # 1. On se connecte discrètement à l'API de CoinGecko (la plus grande base de données crypto)
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={cible}&vs_currencies=eur"
        reponse = requests.get(url)
        donnees = reponse.json()

        # 2. On extrait le prix actuel
        prix_actuel = donnees[cible]['eur']

        print(f"👀 Analyse du marché... Prix actuel : {prix_actuel} €")

        # 3. LA GÂCHETTE
        if prix_actuel <= prix_declenchement:
            print("\n" + "🔥"*10)
            print(f"🚨 BOUM ! CIBLE ATTEINTE ! 🚨")
            print(f"Le prix a chuté à {prix_actuel} € !")
            print("C'est le moment d'acheter !")
            print("🔥"*10 + "\n")
            
            # Le sniper a tiré, on arrête le programme
            break 
        
        # On attend 10 secondes avant de revérifier pour ne pas surcharger le serveur
        time.sleep(10)
        
    except Exception as e:
        # Si le serveur bug ou qu'on perd internet, le script ne plante pas, il met juste un message d'erreur
        print("⚠️ Erreur de connexion au marché, nouvelle tentative...")
        time.sleep(5)