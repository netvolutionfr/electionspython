from resultats import *

'''
Scrutin à un tour : celui qui a le plus de voix l'emporte
'''


def untour(candidats, resultats):
    maximum = 0

    for i in range(len(resultats)):
        if resultats[i]['votes'] > resultats[maximum]['votes']:
            maximum = i

    premier = resultats[maximum]['classement'][0]

    print('Le candidat élu est : ' + candidats[premier])


untour(mescandidats, mesresultats)
