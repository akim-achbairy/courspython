from pwd_tester import Password_Tester
from generator_pwd import Password_Generator
from generator_passphrase import Passphrase_Generator

def main():
    print("Bienvenue sur mon projet de générateur de mots de passe !")

    while True:
        print("\n--- MENU ---")
        print("1) Vérifier un mot de passe")
        print("2) Génération de mot de passe")
        print("3) Génération d'une passphrase via diceware")
        print("4) Quitter")

        choix = input("Votre choix : ").strip()

        if choix == '1':
            # Testeur de mot de passe
            mdp = input("Entrez le mot de passe à vérifier : ")
            t = Password_Tester()
            ent = t.compute_entropy(mdp)
            label = t.get_strength_label(ent)
            print(f"Entropie : {ent:.2f} bits => Force : {label}")

        elif choix == '2':
            # Générateur de mot de passe
            print("Mise en place des paramètres par défaut...")
            gen = Password_Generator()
            mdp_gen = gen.generate_password()
            print(f"Mot de passe généré : {mdp_gen}")

        elif choix == '3':
            # Générateur de passphrase
            print("Génération d'une phrase de 4 mots.")
            passgen = Passphrase_Generator()
            phrase = passgen.generate_passphrase()
            print(f"Notre passphrase : {phrase}")

        elif choix == '4':
            print("A Bientôt !")
            break

        else:
            print("Option invalide ! Réessayez.")

if __name__ == "__main__":
    main()