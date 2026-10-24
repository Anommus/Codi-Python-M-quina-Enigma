def enigma_maquina(text_original, mode="encriptar"):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text_original = text_original.upper() 
    paraula_final = ""
    desplacament = 1

    for lletra in text_original:
        if lletra in alfabet:
            index_lletra = alfabet.index(lletra)
            
            if mode == "encriptar":
                nou_index = (index_lletra + desplacament) % 26
            elif mode == "desencriptar":
                nou_index = (index_lletra - desplacament) % 26
                
            paraula_final += alfabet[nou_index]
        else:
            paraula_final += lletra
            
        desplacament += 1
        if desplacament > 26:
            desplacament = 1

    return paraula_final

# --- INTERACCIÓ AMB L'USUARI ---
missatge = input("Introdueix el missatge que vols processar: ")
mode_escollit = input("Vols 'encriptar' o 'desencriptar'? (Escriu l'opció): ").lower()

if mode_escollit in ["encriptar", "desencriptar"]:
    resultat = enigma_maquina(missatge, mode_escollit)
    print("\n--- RESULTAT ---")
    print(f"Missatge original:  {missatge.upper()}")
    print(f"Missatge processat: {resultat}")
else:
    print("\nError: Opció no vàlida. Has d'escriure 'encriptar' o 'desencriptar'.")