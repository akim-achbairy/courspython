import random
import string

class Password_Generator:
    def __init__(self, nb_min=2, nb_maj=2, nb_numb=2, nb_specials=2):
        # Par défaut : 2 minuscules, 2 maj, 2 chiffres, 2 spéciaux
        self.nb_min = nb_min
        self.nb_maj = nb_maj
        self.nb_numb = nb_numb
        self.nb_specials = nb_specials
        self.special_chars = "!@#$%^&*()-_=+[]{},.;:?/"

    def generate_password(self):
        # Construction du mot de passe
        pwd_list = []

        # Ajout minuscules
        for _ in range(self.nb_min):
            pwd_list.append(random.choice(string.ascii_lowercase))
        # Ajout majuscules
        for _ in range(self.nb_maj):
            pwd_list.append(random.choice(string.ascii_uppercase))
        # Ajout chiffres
        for _ in range(self.nb_numb):
            pwd_list.append(random.choice(string.digits))
        # Ajout caractères spéciaux
        for _ in range(self.nb_specials):
            pwd_list.append(random.choice(self.special_chars))

        # Melange aléatoire
        random.shuffle(pwd_list)

        # Retour de la chaîne finale
        return "".join(pwd_list)