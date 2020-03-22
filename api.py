#quorridor projet 1

import requests


def _url():
    return 'http://www.ulaval.ca'


def _url_base():
    return 'https://python.gel.ulaval.ca/quoridor/api/'


# fonction 3 de 5
def lister_parties(idul):
    rep = requests.get(url=_url_base()+'lister', params={'idul': idul})
    if rep.status_code == 200:
        #Bonne réponse du serveur, décoder JSON
        return rep.json()
    else:
        return(RuntimeError(f"Le GET sur {_url_base()+'lister'} a produit le code d'erreur {rep.status_code}."))


# fonction 4 de 5
def initialiser_partie(idul):
    rep = requests.post(url=_url_base()+'débuter/', data={'idul': idul})
    if rep.status_code == 200:
        #Bonne réponse du serveur, décoder JSON
        try:
            return rep.json()['gagnant']
        except KeyError:
            return rep.json()
    else:
        print(rep.json())
        return "ERROR {}".format(rep.status_code)


# fonction 5 de 5
def jouer_coup(id_partie, type_coup, position):
    rep = requests.post(url=_url_base() + 'jouer/', data={'id': id_partie, 'type': type_coup, 'pos': position})
    if rep.status_code == 200:
        #Bonne réponse du serveur, décoder JSON
        return rep.json()
    else:
        print(rep.json())
        return "ERROR {}".format(rep.status_code)
                            
