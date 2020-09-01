import requests
import json
import myAPIkey


def izdelajZahtevo(start, destinacija, postnasts, postnastd):
    API_KEY = myAPIkey.returnAPIKey()
    modelNiz = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={},{}&destinations={},{}&key={}'.format(start, postnasts, destinacija, postnastd, API_KEY)
    zahtevaJSON = requests.get(modelNiz)
    zahteva = json.loads(zahtevaJSON.text)
    
    if (zahteva['rows'][0]['elements'][0]['status'] == 'NOT_FOUND'):
        return 0
    elif(zahteva['rows'][0]['elements'][0]['status'] == 'ZERO_RESULTS'):
        return -1

    return zahteva
    

def pridobiRazdaljoVKM(start, destinacija, postnasts, postnastd):
    zahteva = izdelajZahtevo(start, destinacija, postnasts, postnastd)

    if(zahteva == 0):
        return 0
    elif(zahteva == -1):
        return -1

    razdalja = (zahteva['rows'][0]['elements'][0]['distance']['text'])

    razdalja = razdalja.replace(' km', '')

    razdalja = float(razdalja)

    return razdalja

    
def pridobiRazdaljoVCasu(start, destinacija, postnasts, postnastd):
    zahteva = izdelajZahtevo(start, destinacija, postnasts, postnastd)

    if(zahteva == 0):
        return 0
    elif(zahteva == -1):
        return -1

    castemp = (zahteva['rows'][0]['elements'][0]['duration']['text'])

    koncni_cas = castemp.replace('s','')

    return koncni_cas