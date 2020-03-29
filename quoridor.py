#quoridor projet 1


import argparse
import api
import pprint as pp

idul = 'donap1'

stade_jeu = {
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
    

# fonction 2 de 5
def afficher_damier_ascii(etat_jeu):
    coord_1 = stade_jeu['joueurs'][0]['pos']
    coord_2 = stade_jeu['joueurs'][1]['pos']
    table = _table_pion()
    tableInterX = _table_interne_x()
    tableInterY1 = _table_interne_x()
    tableInterY2 = _table_interne_y()
    table[str(coord_1[0])][str(coord_1[1])] = '1'
    table[str(coord_2[0])][str(coord_2[1])] = '2'
    murs_horizontaux = []
    murs_verticaux = []
    print(_legende(stade_jeu['joueurs'][0]['nom']))
    print(_top_line())
    for i in stade_jeu['murs']['horizontaux']:
        murs_horizontaux.append(i)

    for i in stade_jeu['murs']['verticaux']:
        murs_verticaux.append(i)
        
    for i in murs_horizontaux:
        tableInterY1[str(i[1])][str(i[0])] = '-'
        tableInterY2[str(i[1])][str(i[0])] = '---'
        tableInterY2[str(i[1])][str(i[0] + 1)] = '---'
    
    for i in murs_verticaux:
        tableInterX[str(i[1])][str(i[0] - 1)] = '|'
        tableInterX[str(i[1] + 1)][str(i[0] - 1)] = '|'
        tableInterY1[str(i[1] + 1)][str(i[0] - 1)] = '|'

    for i in range(9):
        print(str(9 - i) + ' | ', end='')
        for j in range(9):
            print(table[str(j + 1)][str(9 - i)], end=' ')
            print(tableInterX[str(9 - i)][str(j + 1)], end=' ')
        print('')
        if i < 8:
            print('  |', end='')
            for j in range(9):
                print(tableInterY2[str(9 - i)][str(j + 1)], end='')
                print(tableInterY1[str(9 - i)][str(j + 1)], end='')
            print('')
    print(_base_line())
