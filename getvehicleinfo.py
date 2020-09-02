import requests
import xml.etree.ElementTree as ET

tree = None

def pridobi_model(leto, znamka, model):
    model_niz = 'https://www.fueleconomy.gov/ws/rest/vehicle/menu/options?year={}&make={}&model={}'.format(leto, znamka, model)
    request = requests.get(model_niz)

    global tree
    tree = ET.fromstring(request.content)
    texttree = []

    for i in range(len(tree)):
        texttree.append(tree[i][0].text)

    return texttree

def pridobi_litre_na_100km(tree, index):
    ID_modela_avtomobila = tree[index][1].text

    MPG_poizvedba_niz = 'https://www.fueleconomy.gov/ws/rest/vehicle/{}'.format(ID_modela_avtomobila)
    MPG_poizvedba = requests.get(MPG_poizvedba_niz)

    tree1 = ET.fromstring(MPG_poizvedba.content)
    MPG_STANJE = int(tree1[19].text)
    MPG_PRETVORNIK = 235.15
    #MPG je kratica za angleški izraz miles per gallon (tj. milje na galon).

    KONČNO_STANJE = round(MPG_PRETVORNIK / MPG_STANJE, 2)

    return KONČNO_STANJE

def pridobi_strošek(l_na_km, razdalja):
    return round((razdalja / 100) * l_na_km, 2)