<html>
    <head>
    </head>
    <body>
        <h1>Vaša poraba je: {{poraba}} l/100km<h1>

        %if errorcheck == 0:
            <h1>Vnesi pravilne podatke!</h1>
        %elif errorcheck == -1:
            <h1>Potovanje prek cest ni izvedljivo</h1>
        %end
            
        <form action="/last/" method="POST">
            Kraj odhoda: <input name="start" type="text" />
            Postna st.:  <input name="postnasts" type="text" />
            Kraj prihoda:  <input name="destinacija" type="text" />
            Postna st.:  <input name="postnastd" type="text" />
            <input value="Submit" type="submit" />
        </form>
    </body>
</html>