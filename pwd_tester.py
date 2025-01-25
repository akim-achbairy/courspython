import math

class Password_Tester:
    def __init__(self):
        self.thresholds = {
            'FAIBLE': 40,
            'MOYEN': 60
        }

    def compute_entropy(self, password):
        # Calcul de l'entropie basique : longueur * log2 (taille_alphabet)
        # si password vide => entropie = 0
        if not password:
            return 0

        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = lower.upper()
        digits = "0123456789"
        special = "!@#$%^&*()-_=+[]{},.;:?/"
        alphabet_size = 0

        # Minimum une minuscule
        if any(ch in lower for ch in password):
            alphabet_size += 26
        # Minimum une majuscule
        if any(ch in upper for ch in password):
            alphabet_size += 26
        # Minimum de chiffres
        if any(ch in digits for ch in password):
            alphabet_size += 10
        # Caractères spéciaux
        if any(ch in special for ch in password):
            alphabet_size += len(special)

        length = len(password)
        # Entropie = length * log2(alphabet_size)
        # Eviter les crash si alphabet_size=0
        if alphabet_size == 0:
            return 0

        entropy = length * math.log2(alphabet_size)
        return entropy

    def get_strength_label(self, entropy):
        # Selon la valeur, renvoie un label
        if entropy < self.thresholds['FAIBLE']:
            return "Faible"
        elif entropy < self.thresholds['MOYEN']:
            return "Moyen"
        else:
            return "Fort"