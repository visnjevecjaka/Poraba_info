# Poraba_info
Projektna naloga pri predmetu UVP

## Namestitev

Najprej se prepričamo, da imamo na svojem računalniku nameščen bottle. 

Namestimo ga prek ukazne vrstice z ukazom
```
pip install bottle
```

## Uporaba
Po kloniranju repozitorija se v ukazni vrstici do direktorija premaknemo s komando cd,
nato pa poženemo s 
```
./jaka.py
```
Zažene se spletni vmesnik dostopen na [dostop](http://127.0.0.1:8080/), ali pa s klikom na povezavo, ki se izpiše v komandni vrstici.

V polja vnesemo vse potrebne podatke (znamko, model vozila ter leto izdelave), nato pa kliknemo na gumb vnesi. V naslednjem polju se nam v obliki spustnega seznama izpišejo vse različice vnesenega vozila. V primeru, da za vnesene podatke vozilo ni bilo najdeno, se izpiše opozorilo.

Ko izberemo željeno različico vozila, se nam po kliku na gumb izberi odpre nova stran, na kateri vnesemo željen kraj odhoda in prihoda. V primeru, da smo izbrali kraj, katerega ime je pogosto, npr. Gradišče, vnesemo še poštno številko, ki pripomore k natančnosti. Ko smo vnesli potrebne podatke, kliknemo vnesi.

Prikaže se nam zadnja stran, na kateri se nam izpiše izračunana poraba, razdalja med krajema v kilometrih ter čas potovanja in cena porabljenega goriva.

## Licenca
[MIT](https://choosealicense.com/licenses/mit/)






