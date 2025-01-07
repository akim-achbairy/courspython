from qcm.question import Question
from qcm.quiz import Quiz

def main():
    quiz = Quiz()

    # Ajout des questions
    quiz.add_question(Question("Quelle est la capitale de la France ?", ["Paris", "Londres", "Washington D.C"], "a"))
    quiz.add_question(Question("Combien font 250 % 2 ?", ["0", "3", "1"], "a"))
    quiz.add_question(Question("Quelle est la couleur du cheval d'Henry IV ?", ["Noir", "Rouge", "Blanc"], "c"))
    quiz.add_question(Question("Qui a réalisé le film 'Pulp Fiction' ?", ["Tarantino", "Spielberg", "Coppola"], "a"))
    quiz.add_question(Question("Quel père fondateur américain a crée le New York Post ?", ["Thomas Jefferson", "Alexander Hamilton", "Jon Adams"], "b"))
    quiz.add_question(Question("Quel dictateur a déclenché une guérrilla civile afin de monter au pouvoir ?", ["Hitler", "Castro", "Michael Jordan"], "b"))
    quiz.add_question(Question("Qui est à l'origine des musiques originales de la comédie musicale 'In The Heights' ?", ["Lin Manuel-Miranda", "Jonathan Larson", "Stephen Sondheim"], "a"))
    quiz.add_question(Question("Qui était le 2ème président des Etats-Unis d'Amérique ?", ["Thomas Jefferson", "Jon Adams", "Georges Washington"], "b"))
    quiz.add_question(Question("Qui était le 4ème président des Etats-Unis d'Amérique ?", ["Thomas Jefferson", "Jon Adams", "James Madison"], "c"))
    quiz.add_question(Question("Quel est la caractéristique de l'épouvantail dans le Magicien d'Oz ?", ["Il n'a pas d'argent", "Il n'a pas de cervelle", "Il n'a pas de coeur"], "b"))


    # Lancement du quiz
    quiz.start()

if __name__ == "__main__":
    main()