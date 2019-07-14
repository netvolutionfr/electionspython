from resultats import *
import itertools

'''
système de Condorcet : chaque candidat est opposé à tous les autres et celui qui
emporte le plus de duels gagne.
'''


def evalue_duel(candidat1, candidat2, resultats):
    scoresduel = [0, 0]
    # parcourir tous les résultats
    for resultat in resultats:
        classement = resultat['classement']
        # pour chaque classement, déterminer qui est le meilleur candidat des deux et lui ajouter un point
        i = 0
        attribue = False
        while i < len(classement) and not attribue:
            if classement[i] == candidat1:
                scoresduel[0] = scoresduel[0] + resultat['votes']
                attribue = True
            else:
                if classement[i] == candidat2:
                    scoresduel[1] = scoresduel[1] + resultat['votes']
                    attribue = True
            i = i+1
    return scoresduel


def condorcet(candidats, resultats):
    # initialisation du tableau de scores
    scores = list()
    for i in range(len(candidats)):
        scores.append(0)

    duels = list((i, j) for ((i, _), (j, _)) in itertools.combinations(enumerate(candidats), 2))
    for duel in duels:
        resultatduel = evalue_duel(duel[0], duel[1], resultats)
        scores[duel[0]] = scores[duel[0]] + resultatduel[0]
        scores[duel[1]] = scores[duel[1]] + resultatduel[1]

    # on détermine le candidat qui a le meilleur score
    maximum = 0
    for i in range(len(scores)):
        if scores[i] > scores[maximum]:
            maximum = i
    print("Le candidat élu est " + candidats[maximum])


condorcet(mescandidats, mesresultats)

