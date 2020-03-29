#quorridor projet 1
import api
import quoridor
import pprint as pp

def main():
    command = analyser_commande()
    debut = api.lister_parties(command.idul)
    pp.pprint(debut)
    afficher_damier_ascii(debut['parties'][0]['état'])
    for i in debut['parties']:
        if i['id'] == id:
            afficher_damier_ascii(i['état'])
    while True:
        print("Type de coup ['D', 'MH', 'MV']: ")
        type_coup = input()
        print("Position x: ")
        position_x = int(input())
        print("Position y: ")
        position_y = int(input())
        position = (position_x, position_y)
        pp.pprint(api.jouer_coup(id, type_coup, position))
        etat = api.lister_parties(command.idul)
        for i in etat['parties']:
            if i['id'] == id:
                afficher_damier_ascii(i['état'])


if __name__ == '__main__':
    main()
