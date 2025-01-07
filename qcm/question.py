import random

class Question:
    def __init__(self, text, options, correct_answer):
        """
        text: str, le texte de la question
        options: list[str], les trois options de réponse
        correct_answer: str, la réponse correcte ('a', 'b'ou 'c')
        """
        self.text = text
        self.options = options
        self.correct_answer = correct_answer.lower()

    def is_correct(self, answer):
        """Vérifie si la réponse donnée est correcte."""
        return answer.lower() == self.correct_answer

    def shuffle_options(self):
        """Mélange les options pour chaque question."""
        zipped = list(zip(['a', 'b', 'c'], self.options))
        random.shuffle(zipped)
        shuffled_keys, shuffled_options = zip(*zipped)
        self.options = list(shuffled_options)
        self.correct_answer = ['a', 'b', 'c'][list(shuffled_keys).index(self.correct_answer)] 