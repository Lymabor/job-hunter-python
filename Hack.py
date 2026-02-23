import time

# 1. La cible
mot_de_passe_secret = "73928"
tentatives = 0

print("🚨 DÉMARRAGE DE L'ATTAQUE BRUTE-FORCE 🚨")
time.sleep(1) # Petite pause pour le suspense

# 2. L'attaque (On teste les 10 000 possibilités de 0000 à 9999)
for i in range(100000):
    tentatives += 1
    
    # On formate le nombre pour qu'il ait toujours 4 chiffres (ex: 7 devient 0007)
    code_teste = str(i).zfill(4) 
    
    # On affiche ce que fait la machine (Effet Matrix garanti)
    print(f"[!] Essai en cours : {code_teste}")
    
    # 3. La vérification
    if code_teste == mot_de_passe_secret:
        print("\n" + "="*40)
        print(f"✅ BINGO ! ACCÈS AUTORISÉ.")
        print(f"🔓 Le code secret est : {code_teste}")
        print(f"⏱️ Craqué en {tentatives} tentatives.")
        print("="*40 + "\n")
        break # On arrête le programme, on a gagné

        