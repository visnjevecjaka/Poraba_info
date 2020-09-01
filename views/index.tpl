<!DOCTYPE html>
<html lang="sl">
    <head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="/static/index.css">
    <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Lato">
    </head>

    <body>

    <div class="naslov">
        <h1>PORABA - INFO</h1>
    </div>

    <div class="napis">
        %if seznam == []:
            <h1>Vnesi pravilne podatke!</h1>
        %end
    </div>
    <div class="anketa">
        <form action="/" method="POST">
            <label for="znamka">Znamka:</label>
            <input id="znamka" name="Znamka" type="text" placeholder="Ford" />
            <label for="model">Model:</label>
            <input id="model" name="Model" type="text" placeholder="Mustang"/>
            <label for="leto">Leto:</label>
            <input id="leto" name="Leto" type="text" placeholder="2020"/>
            <input id="submit" value="Vnesi" type="submit"/>
        </form>
    </div>

    <div class="anketa">
        <form action="/next/" method="POST">
            <select class="option" name="izbor">
            % for i in seznam:
                <option value="{{i}}">{{i}}</option>
            % end
            </select>
            <input id="submit" value="Izberi" type="submit"/>
        </form>
    </div>
    </body>
</html>