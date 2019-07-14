from resultats import *

'''
système de Borda : chaque électeur attribue N points pour celui qu’il place en tête,
N-1 pour le 2nd, ... jusqu’à 1 point pour le dernier. Le vainqueur est celui qui a le plus
de points.
'''


def borda(candidats, resultats):
    # initialisation du tableau de scores
    scores = list()
    for i in range(len(candidats)):
        scores.append(0)

    for i in range(len(resultats)):
        for j in range(len(candidats)):
            classement = resultats[i]['classement']
            scores[classement[j]] += (len(candidats) - j) * resultats[i]['votes']

    # rechercher le maximum du tableau scores
    maximum = 0
    for i in range(len(scores)):
        if scores[i] > scores[maximum]:
            maximum = i
    print("Le candidat élu est " + candidats[maximum] + " avec un score de " + str(scores[maximum]))


borda(mescandidats, mesresultats)
