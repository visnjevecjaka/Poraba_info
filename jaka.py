from bottle import run, route, request, template, static_file
import getvehicleinfo
import getdistanceinfo


@route('/static/<filename:path>')
def staticindex(filename):
    return static_file(filename, root='static/')

Info = {}
seznamleto = []
seznamznamka = []
seznammodel = []
izbor = []
leto = 0
poraba = None

@route('/')
def index():
    global Info
    global seznamleto
    global seznamznamka
    global seznammodel
    seznamleto = getvehicleinfo.getYear()
    Info["seznamleto"] = seznamleto
    Info["seznamznamka"] = seznamznamka
    Info["seznammodel"] = seznammodel
    Info["izbor"] = izbor
    return template('views/index.tpl', Info)

@route('/', method='POST')
def do_index():
    global Info
    global seznamznamka
    global seznammodel
    
    leto = request.forms.get("leto")
    znamka = request.forms.get("znamka")
    model = request.forms.get("model")
    
    seznamznamka = getvehicleinfo.getMake(leto)
    seznammodel = getvehicleinfo.getModel(znamka)
    izbor = getvehicleinfo.getModelInfo(model)

    Info["seznamznamka"] = seznamznamka
    Info["seznammodel"] = seznammodel
    Info["izbor"] = izbor

    return template('views/index.tpl', Info)

@route('/next/', method='POST')
def getresult():
    izbor = request.forms.get('izbor')
    index = -1
    for i in range(len(seznammodel)):
        if (seznammodel[i] == izbor):
            index = i
    
    global poraba
    poraba = getvehicleinfo.getl100km(getvehicleinfo.tree, index)
    return template('views/second.tpl', poraba=poraba, errorcheck = -2)

@route('/last/', method='POST')
def getfinal():
    start = request.forms.getunicode('start')
    postnasts = request.forms.get('postnasts')
    destinacija = request.forms.getunicode('destinacija')
    postnastd = request.forms.get('postnastd')

    if(start == '' or destinacija == ''):
        return template('views/second.tpl', poraba=poraba, errorcheck = 0)

    VKM = getdistanceinfo.pridobiRazdaljoVKM(start, destinacija, postnasts, postnastd)
    VHM = getdistanceinfo.pridobiRazdaljoVCasu(start, destinacija, postnasts, postnastd)

    if (VKM == 0 or VHM == 0):
        return template('views/second.tpl', poraba=poraba, errorcheck = 0)
    elif(VKM == -1 or VHM == -1):
        return template('views/second.tpl', poraba=poraba, errorcheck = -1)
    
    cost = getvehicleinfo.getcost(poraba, VKM)

    return template('views/last.tpl', poraba=poraba, VKM=VKM, VHM=VHM, cost=cost, znamka=znamka,
    model=model, leto=leto, start=start, destinacija=destinacija)



if __name__ == '__main__':
    run()