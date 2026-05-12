#!/usr/bin/python3

import cgi

form = cgi.FieldStorage()
matrikelnummer = form.getvalue("Matrikelnummer")

print("Content-type: text/html")
print()

print(f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Ausgabe</title>
</head>
<body>

<h1>Eingegebene Daten</h1>

<ul>
    <li>Matrikelnummer: {matrikelnummer}</li>

  </ul>

</body>
</html>
""")
