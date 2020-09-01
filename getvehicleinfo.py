import requests
import xml.etree.ElementTree as ET

tree = None

def getCorrectModel(year, make, model):
    modelString = 'https://www.fueleconomy.gov/ws/rest/vehicle/menu/options?year={}&make={}&model={}'.format(year, make, model)
    request = requests.get(modelString)

    global tree
    tree = ET.fromstring(request.content)
    texttree = []

    for i in range(len(tree)):
        texttree.append(tree[i][0].text)

    print(texttree)

    return texttree

def getl100km(tree, index):
    modelNr = tree[index][1].text
    # print(modelNr)

    MPGPoizvedbaString = 'https://www.fueleconomy.gov/ws/rest/vehicle/{}'.format(modelNr)
    MPGPoizvedba = requests.get(MPGPoizvedbaString)

    tree1 = ET.fromstring(MPGPoizvedba.content)
    FINAL_MPG = int(tree1[19].text)
    MPGCONVERTOR = 235.15

    FINALL100KM = round(MPGCONVERTOR / FINAL_MPG, 2)

    return FINALL100KM

def getcost(lkm, distance):
    return round((distance/100) * lkm, 2)