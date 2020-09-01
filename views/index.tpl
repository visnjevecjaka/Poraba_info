<html>
    <head>
    </head>
    <body>
        %if seznam == []:
            <h1>Vnesi pravilne podatke!</h1>
        %end
        <form action="/" method="POST">
            Znamka: <input name="Znamka" type="text" />
            Model: <input name="Model" type="text"/>
            Leto: <input name="Leto" type="text"/>
            <input value="Submit" type="submit"/>
        </form>
        <form action="/next/" method="POST">
            <select name="izbor">
            % for i in seznam:
                <option value="{{i}}">{{i}}</option>
            % end
            </select>
            <input value="Submit" type="submit"/>
        </form>
    </body>
</html>