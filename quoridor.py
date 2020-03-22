#quoridor projet 1


import argparse
import api
import pprint as pp

idul = 'donap1'

etatactuel = {
"joueurs": [
{"nom": "idul", "murs": 7, "pos": [5, 5]},
{"nom": "automate", "murs": 3, "pos": [8, 6]}],
"murs": {
"horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
"verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]}
}

# fonction 1 de 5
def analyser_commande():
    parser = argparse.ArgumentParser(description='Jeu Quoridor')
    parser.add_argument('-i', '--idul', metavar='TYPE', dest='idul',
                        default='donap1', choices = ['type1', 'type 2'],help="Idul du joueur")          
    return parser.parse_args()


# création de la table 
def _legende(idul):
    return "legende: 1={}, 2=automate".format(idul)

def _top_line():
    ligne = '   '+'-'*35
    return ligne

def _table_pion():
    lignes = {}
    for x in range(1, 10):
        colonnes = {}
        for y in range(1, 10):
            colonnes[str(y)] = '.'
        lignes[str(10-x)] = colonnes
    return lignes

def _base_line():
    ligne = '--|'+'-'*35+'\n'+'  | 1   2   3   4   5   6   7   8   9'
    return ligne

def _table_interne_x():
    lignes = {}
    for x in range(1, 10):
        colonnes = {}
        for y in range(1, 10):
            if y == 9:
                colonnes[str(y)] = '|'
            else:
                colonnes[str(y)] = ' '
        lignes[str(10-x)] = colonnes
    return lignes

def _table_interne_y():
    lignes = {}
    for x in range(1, 10):
        colonnes = {}
        for y in range(1, 10):
            colonnes[str(y)] = '   '
        lignes[str(10-x)] = colonnes
    return lignes
