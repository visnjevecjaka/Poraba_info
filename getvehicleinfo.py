import requests
import xml.etree.ElementTree as ET

tree = None
year = None
make = None
model = None

def getYear():
    modelString = 'https://www.fueleconomy.gov/ws/rest/vehicle/menu/year'
    request = requests.get(modelString)

    tree = ET.fromstring(request.content)
    texttree = []

    for i in range(len(tree)):
        texttree.append(tree[i][0].text)

    print(texttree)

    return texttree

def getMake(finalyear):
    modelString = 'https://www.fueleconomy.gov/ws/rest/vehicle/menu/make?year={}'.format(finalyear)
    request = requests.get(modelString)
    print(modelString)
    global year
    year = finalyear

    tree = ET.fromstring(request.content)
    texttree = []

    for i in range(len(tree)):
        texttree.append(tree[i][0].text)

    return texttree

def getModel(finalmake):
    modelString = 'https://www.fueleconomy.gov/ws/rest/vehicle/menu/model?year={}&make={}'.format(year, finalmake)
    request = requests.get(modelString)
    print(modelString)

    global make
    make = finalmake

    tree = ET.fromstring(request.content)
    texttree = []

    for i in range(len(tree)):
        texttree.append(tree[i][0].text)

    return texttree

def getModelInfo(finalmodel):
    modelString = 'https://www.fueleconomy.gov/ws/rest/vehicle/menu/options?year={}&make={}&model={}'.format(year, make, finalmodel)
    request = requests.get(modelString)
    print(modelString)

    global model
    model = finalmodel

    tree = ET.fromstring(request.content)
    texttree = []

    for i in range (len(tree)):
        texttree.append(tree[i][0].text)

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