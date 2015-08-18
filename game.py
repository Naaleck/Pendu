"""Main code of the game"""

import os
import pickle
import functions, data
import re


# Checking if scores file exists
if not os.path.isfile(data.scores_file):
    with open(data.scores_file, 'wb') as file:
        pickler = pickle.Pickler(file)
        pickler.dump({})

print("Bienvenue dans le jeu du Pendu")
name = input("Entrez votre nom\n")

# Checking if the name is in the file
scores = functions.get_scores(data.scores_file)

if name not in scores:
    scores[name] = 0
else:
    print("Bienvenue {} ! Score : {} points.".format(name, scores[name]))

print("\n\n")

# Game
while data.replay:
    # Getting random word
    rdm_word = functions.get_random_word(data.words)
    hidden_word = functions.get_hidden_word(rdm_word)
    chances = data.chances

    print("Le mot a deviner est {} ({})".format(rdm_word, hidden_word))
    print("Chances restantes : ", chances)

    while chances > 0 and rdm_word != hidden_word:
        # Asking for a letter
        while 1:
            letter = input("Saisissez une lettre ")

            if len(letter) == 1 and not letter.isdigit():
                break

        occ = [m.start() for m in re.finditer(letter, rdm_word)]

        if occ:  # Letter found
            for index in occ:
                hidden_word = hidden_word[:index] + letter + hidden_word[index+1:]

        chances -= 1

        print(hidden_word)
        print("Chances restantes : ", chances)

    # Handling the scores
    if chances > 0:
        scores[name] += chances
        print("Bravo {}, le mot a deviner etait \"{}\", vous avez gagne {} point(s)\n\n".format(name, rdm_word, chances))
    else:
        print("Vous n'avez plus de chances, le mot a deviner etait \"{}\".\n\n".format(rdm_word))

    functions.save_scores(data.scores_file, scores)

    # Asking for replay
    rply = input("Voulez-vous rejouer ? (o/n) ")

    if rply.lower() == "n":
        data.replay = False


# Pausing
os.system("pause")
