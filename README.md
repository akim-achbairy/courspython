# Créateur de Mots de Passe et Passphrases

Ce projet offre un générateur de mots de passe sécurisés ainsi qu'un générateur de passphrases utilisant la méthode Diceware.

## Caractéristiques
- Création de mots de passe intégrant des caractères sur mesure (lettres capitales, lettres minuscules, chiffres, symboles).
- Création de phrases de passe aléatoires en se servant de la méthode Diceware.
- Outil d'évaluation de la robustesse des mots de passe basé sur l'entropie.

## Organisation du Projet
- `main.py` : Point de départ pour le lancement du programme.
- `generator_pwd.py` : Créateur de mots de passe.
- `generator_passphrase.py` : Créateur de phrases de passe basé sur Diceware.
- `pwd_tester.py` : Outil d'évaluation de mots de passe.
- `data_lancee.py` : Dictionnaire Diceware intégral (7776 combinaisons).

## Mode d'emploi
1. Lancez le fichier `main.py`.
2. Suivez les directives pour la création ou l'évaluation de mots de passe/passphrases.

## Lancement 
```bash
python3 main.py
