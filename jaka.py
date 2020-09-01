from bottle import run, route, request, template, static_file
import getvehicleinfo
import getdistanceinfo


@route('/static/<filename:path>')
def staticindex(filename):
    return static_file(filename, root='static/')

@route('/')
def index():
    seznam=[' ']
    Info = {}
    Info["seznam"] = seznam
    return template('views/index.tpl', Info)

seznam = None
poraba = None

@route('/', method='POST')
def do_index():
    znamka = request.forms.get('Znamka')
    model = request.forms.get('Model')
    leto = request.forms.get('Leto')
    izbor = request.forms.get('izbor')

    global seznam
    seznam = getvehicleinfo.getCorrectModel(leto, znamka, model)
    Info = {}
    Info["seznam"] = seznam

    return template('views/index.tpl', Info)

@route('/next/', method='POST')
def getresult():
    izbor = request.forms.get('izbor')
    index = -1
    for i in range(len(seznam)):
        if (seznam[i] == izbor):
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

    return template('views/last.tpl', poraba=poraba, VKM=VKM, VHM=VHM, cost=cost)



if __name__ == '__main__':
    run()