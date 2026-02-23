import wikipedia
import time

# 1. On configure le cerveau en français
wikipedia.set_lang("fr")

print("\n" + "🧠"*3)
print("ASSISTANT UNIVERSITAIRE CONNECTÉ")
print("Je peux résumer n'importe quel concept pour tes cours.")
print("🧠"*3 + "\n")

# 2. Le script TE pose une question et attend ta réponse
sujet = input("👉 Quel concept dois-je chercher et résumer pour toi ? : ")

print(f"\n⏳ Analyse de la base de données mondiale pour '{sujet}'...")
time.sleep(1) # Laisse le temps au script de chercher

try:
    # 3. L'extraction : On demande expressément seulement les 3 premières phrases (l'essentiel)
    resume = wikipedia.summary(sujet, sentences=3)
    
    # 4. L'affichage propre pour tes fiches de révision
    print("\n" + "="*60)
    print(f"📖 FICHE EXPRESS : {sujet.upper()}")
    print("="*60)
    print(resume)
    print("="*60 + "\n")

# Sécurités : si tu tapes un mot qui n'existe pas ou qui a trop de sens
except wikipedia.exceptions.PageError:
    print("\n❌ Cible introuvable. Ce concept n'existe pas ou est mal orthographié.")
except wikipedia.exceptions.DisambiguationError:
    print("\n⚠️ Le terme est trop vague (ex: 'Pomme' peut être le fruit ou l'entreprise). Sois plus précis !")