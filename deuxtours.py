from resultats import *

'''
élection à deux tours : les deux candidats placés en tête au 1er tour sont qualifiés
pour le 2nd, ceux qui ont voté pour les autres candidats reportent leur voix sur celui
ou celle qu’ils avaient mis devant au 1er tour.
'''


def deuxtours(candidats, resultats):
    # premier tour : sélectionner les 2 premiers candidats
    print('Premier tour')

    premier = 0
    for i in range(len(resultats)):
        if resultats[i]['votes'] > resultats[premier]['votes']:
            premier = i

    resultats[premier], resultats[0] = resultats[0], resultats[premier]

    deuxieme = 1
    for i in range(1, len(resultats)):
        if resultats[i]['votes'] > resultats[deuxieme]['votes']:
            deuxieme = i

    candidatpremier = resultats[premier]['classement'][0]
    candidatdeuxieme = resultats[deuxieme]['classement'][0]

    print('Candidats sortis du premier tour : ' + candidats[candidatpremier] + ' et ' + candidats[candidatdeuxieme])

    # deuxieme tour : report des voix

    print('Deuxième tour')

    # Pour chaque résultat, on cherche qui de candidat 1 ou de candidat 2 est en premier,
    # on lui ajoute le nombre de voix

    scorepremier = 0
    scoredeuxieme = 0

    for i in range(len(resultats)):
        classement = resultats[i]['classement']
        score = resultats[i]['votes']
        j = 0
        attribue = False
        while j < len(classement) and not attribue:
            if classement[j] == candidatpremier:
                scorepremier += score
                attribue = True
            else:
                if classement[j] == candidatdeuxieme:
                    scoredeuxieme += score
                    attribue = True
            j = j+1

    if scorepremier > scoredeuxieme:
        print('Le candidat élu est : ' + candidats[candidatpremier])
    else:
        print('Le candidat élu est : ' + candidats[candidatdeuxieme])


deuxtours(mescandidats, mesresultats)
