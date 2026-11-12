import json


def recuperer_carte(nom):
    with open('carte.json') as f:
        json_str = f.read()
        return json.loads(json_str)[nom]


class Carte:
    def __init__(self,nom):
        self.nom = nom
        carte = recuperer_carte(nom)
        if carte["effect"]:
            self.effect = carte["effect"]

if __name__ == '__main__':
    test = Carte('Cancer')
    print(test.effect)