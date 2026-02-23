import pyttsx3

print("\n" + "🎙️"*3)
print("MODULE VOCAL ACTIVÉ (VERSION ANTI-BUG)")
print("Tape 'stop' pour désactiver l'IA.")
print("🎙️"*3 + "\n")

while True:
    texte = input("🤖 Que dois-je dire, Boss ? : ")
    
    if texte.lower() == 'stop':
        print("Arrêt du système. À bientôt.")
        break
        
    # --- LE HACK COMMENCE ICI ---
    # 1. On fabrique un tout nouveau moteur pour cette phrase précise
    moteur = pyttsx3.init()
    moteur.setProperty('rate', 170)
    
    # 2. On le fait parler
    moteur.say(texte)
    moteur.runAndWait()
    
    # 3. On détruit purement et simplement le moteur pour éviter le bug !
    del moteur
    # ----------------------------