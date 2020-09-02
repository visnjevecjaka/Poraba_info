from bottle import run, route, request, template, static_file
import getvehicleinfo
import getdistanceinfo


@route('/static/<filename:path>')
def staticindex(filename):
    return static_file(filename, root='static/')

@route('/')
def index_prva():
    seznam=[' ']
    Info = {}
    Info["seznam"] = seznam
    return template('views/index.tpl', Info)

seznam = None
poraba = None
znamka = None
model = None
leto = None

@route('/', method='POST')
def index_druga():
    global znamka
    global model
    global leto
    znamka = request.forms.get('Znamka')
    model = request.forms.get('Model')
    leto = request.forms.get('Leto')
    izbor = request.forms.get('izbor')

    global seznam
    seznam = getvehicleinfo.pridobi_model(leto, znamka, model)
    Info = {}
    Info["seznam"] = seznam

    return template('views/index.tpl', Info)

@route('/next/', method='POST')
def pridobi_rezultat():
    izbor = request.forms.get('izbor')
    index = -1
    for i in range(len(seznam)):
        if seznam[i] == izbor:
            index = i
    
    global poraba
    poraba = getvehicleinfo.pridobi_litre_na_100km(getvehicleinfo.tree, index)
    return template('views/second.tpl', poraba=poraba, errorcheck = -2)

@route('/last/', method='POST')
def pridobi_končni_rezultat():
    start = request.forms.getunicode('start')
    postnasts = request.forms.get('postnasts')
    destinacija = request.forms.getunicode('destinacija')
    postnastd = request.forms.get('postnastd')

    if start == '' or destinacija == '':
        return template('views/second.tpl', poraba=poraba, errorcheck = 0)

    VKM = getdistanceinfo.pridobi_razdaljo_v_km(start, destinacija, postnasts, postnastd)
    VHM = getdistanceinfo.pridobi_razdaljo_v_času(start, destinacija, postnasts, postnastd)

    if VKM == 0 or VHM == 0:
        return template('views/second.tpl', poraba=poraba, errorcheck = 0)
    elif VKM == -1 or VHM == -1:
        return template('views/second.tpl', poraba=poraba, errorcheck = -1)
    
    strošek = getvehicleinfo.pridobi_strošek(poraba, VKM)

    return template('views/last.tpl', poraba=poraba, VKM=VKM, VHM=VHM, strošek=strošek, znamka=znamka,
    model=model, leto=leto, start=start, destinacija=destinacija)



if __name__ == '__main__':
    run()