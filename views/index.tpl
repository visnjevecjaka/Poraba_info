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

    <div class="anketa">
        <form action="/" method="POST">
            <label for="leto">Leto:</label>
            <select class="option" name="leto">
            % for i in seznamleto:
                <option value="{{i}}">{{i}}</option>
            % end
            <input type="submit"</>  
        </form>

        <form action="/" method="POST">
            <label for="znamka">Znamka:</label>
            <select class="option" name="znamka">
            % for i in seznamznamka:
                <option value="{{i}}">{{i}}</option>
            %end
            <input type="submit"</>
        </form>

        <form action="/" method="POST">
            <label for="model">Model:</label>
            <select class="option" name="model">
            % for i in seznammodel:
                <option value="{{i}}">{{i}}</option>
            %end
            <input type="submit"</>
        </form>

        <form action="/next/" method="POST">
            <select class="option" name="izbor">
            % for i in izbor:
                <option value="{{i}}">{{i}}</option>
            %end
            <input type="submit"</>
        </form>
    </div>
    </body>
</html>