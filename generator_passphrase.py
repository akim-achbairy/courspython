import random
from data_lancee import diceware

class Passphrase_Generator:
    def __init__(self, nb_words=4):
        self.nb_words = nb_words  # Par défaut, 4 mots dans la passphrase

    def generate_passphrase(self):
        words = []
        for _ in range(self.nb_words):
            # Simulation de lancée de 5 dés (valeurs 1 à 6)
            dice_code = ''.join(str(random.randint(1, 6)) for _ in range(5))

            # Si le code est dans le dictionnaire, on prend le mot attendu
            if dice_code in diceware:
                words.append(diceware[dice_code])
            else:
                # si c'est un code non trouvé
                words.append("???")

        # Renvoie de la passphrase
        return " ".join(words)