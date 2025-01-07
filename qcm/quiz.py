from qcm.question import Question
import random

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.user_answers = []  # Stocke les réponses de l'utilisateur

    def add_question(self, question):
        """Ajoute une question au quiz."""
        self.questions.append(question)

    def start(self):
        random.shuffle(self.questions)
        for i, question in enumerate(self.questions):
            question.shuffle_options()
            print(f"Question {i + 1}: {question.text}")
            for idx, option in enumerate(['a', 'b', 'c']):
                print(f"  {option}. {question.options[idx]}")

            user_answer = input("Votre réponse (a/b/c) : ").strip().lower()
            while user_answer not in ['a', 'b', 'c']:
                user_answer = input("Veuillez entrer a, b ou c : ").strip().lower()

            # Enregistre la réponse de l'utilisateur
            self.user_answers.append((question, user_answer))

            if question.is_correct(user_answer):
                print("Bonne réponse !")
                self.score += 1
            else:
                print(f"Mauvaise réponse. La bonne réponse était : {question.correct_answer}")
            print()

        self.show_results()

    def show_results(self):
        print(f"Votre score final est de {self.score}/{len(self.questions)}\n")
        print("Corrigé :")
        for i, (question, user_answer) in enumerate(self.user_answers):
            correct_letter = question.correct_answer
            correct_option = question.options[['a', 'b', 'c'].index(correct_letter)]
            print(f"Question {i + 1}: {question.text}")
            print(f"  Votre réponse : {user_answer.upper()} ({question.options[['a', 'b', 'c'].index(user_answer)]})")
            print(f"  Bonne réponse : {correct_letter.upper()} ({correct_option})\n")
