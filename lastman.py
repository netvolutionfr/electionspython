from resultats import *

'''
système à plusieurs tours par élimination (“last man standing”) : à chaque tour, on
élimine celui qui a le moins de voix, jusqu’à ce qu’il n’en reste qu’un, les électeurs
gardant leur ordre de préférence.
'''


def lastmanstanding(candidats, resultats):
    print(resultats)
    if len(resultats) == 2:
        if resultats[0]['votes'] > resultats[1]['votes']:
            gagnant = resultats[0]['classement'][0]
        else:
            gagnant = resultats[1]['classement'][0]

        print('Le gagnant est : ' + candidats[gagnant])
    else:
        # initialisation du tableau de scores
        scores = list()
        for i in range(len(candidats)):
            scores.append(0)
        for resultat in resultats:
            gagnant = resultat['classement'][0]
            scores[gagnant] = scores[gagnant] + resultat['votes']

        # on trouve le perdant en cherchant le minimum des scores
        perdant = 0
        for i in range(len(scores)):
            if 0 < scores[i] < scores[perdant]:
                perdant = i
        print('Candidat éliminé : ' + candidats[perdant])

        # on crée un nouveau dict de résultats sans le perdant
        newresultats = []
        for resultat in resultats:
            if resultat['classement'][0] != perdant:
                newresultat = resultat
                newclassement = []
                for i in range(len(newresultat['classement'])):
                    if newresultat['classement'][i] != perdant:
                        newclassement.append(newresultat['classement'][i])
                newresultat['classement'] = newclassement
                newresultats.append(newresultat)

        # on reporte les voix
        for resultat in resultats:
            if resultat['classement'][0] == perdant:
                second = resultat['classement'][1]
                for newresultat in newresultats:
                    if newresultat['classement'][0] == second:
                        newresultat['votes'] = newresultat['votes'] + resultat['votes']

        # on appelle la fonction de manière récursive
        lastmanstanding(candidats, newresultats)


lastmanstanding(mescandidats, mesresultats)
