# Poraba_info
Projektna naloga pri predmetu UVP na Fakulteti za matematiko in fiziko v študijskem letu 2019/20.

## Kratek opis 
Poraba-info je spletna stran, ki uporabniku omogoča izračun stroškov porabe goriva na določeni poti med dvema krajema. Poleg tega uporabnik dobi povratno informacijo o potovalnem času ter dolžini poti, ki je mora opraviti. 

## Namestitev
Najprej se prepričajmo, da imamo na svojem računalniku nameščen bottle. 

Namestimo ga prek ukazne vrstice z ukazom
```
pip install bottle
```

## Uporaba
Po kloniranju repozitorija se v ukazni vrstici do direktorija premaknemo z ukazom cd,
nato pa poženemo s 
```
python jaka.py
```
Zažene se spletni vmesnik, dostopen na [dostop](http://127.0.0.1:8080/), lahko pa ga zaženemo tudi s klikom na povezavo, ki se izpiše v ukazni vrstici.

V polja vnesemo vse potrebne podatke (znamko vozila, model vozila ter leto izdelave), nato pa kliknemo na gumb vnesi. V naslednjem polju se nam v obliki spustnega seznama izpišejo vse različice vnesenega vozila. V primeru, da za vnesene podatke vozilo ni bilo najdeno, se izpiše opozorilo.

Ko izberemo željeno različico vozila, se nam po kliku na gumb izberi odpre nova stran, na kateri vnesemo željen kraj odhoda in prihoda. V primeru, da smo izbrali kraj, katerega ime je pogosto, npr. Gradišče, vnesemo še poštno številko, ki pripomore k natančnosti. Ko smo vnesli potrebne podatke, kliknemo vnesi.

Prikaže se nam zadnja stran, na kateri se nam izpiše izračunana poraba, razdalja med krajema v kilometrih, čas potovanja in cena porabljenega goriva.

## Licenca
[MIT](https://choosealicense.com/licenses/mit/)






