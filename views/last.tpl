<!DOCTYPE html>
<html lang="sl">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="/static/last.css">
        <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Lato">
    </head>
    <body>
    <div class="container">
        <h1 class="podatki">{{znamka}} {{model}} {{leto}}</h1>
        <h1 class="podatki">Vaša poraba je {{poraba}} l/100 km.<h1>
        <h1 class="podatki">Razdalja med krajema {{start}} in {{destinacija}} je {{VKM}} km.</h1>
        <h1 class="podatki">Trajanje poti je {{VHM}}.</h1>
        <h1 class="podatki">Vaš strošek: {{cost}} €</h1>
    </div>
    </body>
</html>