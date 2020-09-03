<!DOCTYPE html>
<html lang="sl">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="/static/second.css">
        <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Lato">
    </head>

    <body>

        <h1 class="poraba">Vaša poraba je {{poraba}} l/100 km.<h1>

        <div class="error">
        %if errorcheck == 0:
            <h1>Vnesi pravilne podatke!</h1>
        %elif errorcheck == -1:
            <h1>Potovanje prek cest ni izvedljivo</h1>
        %end
        </div>
        
        <div class="anketa">
        <form action="/last/" method="POST">
            <label for="start">Kraj odhoda:</label>
            <input id="start" name="start" type="text" placeholder="Koper" />
            <label for="postnasts">*Poštna številka:</label>
            <input id="postnasts" name="postnasts" type="text" placeholder="6000"/>
            <label for="destinacija">Kraj prihoda:</label>
            <input id="destinacija" name="destinacija" type="text" placeholder="Ljubljana"/>
            <label for="postnastd">*Poštna številka:</label>
            <input id="postnastd" name="postnastd" type="text" placeholder="1000"/>
            <h1 class="poraba">*Podatek potreben le za kraje s pogostimi imeni</h1>
            <input id="submit" value="Vnesi" type="submit" />
        </form>
        </div>
    </body>
</html>