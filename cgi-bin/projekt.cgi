#!/usr/bin/python3

import cgi

form = cgi.FieldStorage()
matrikelnummer = form.getvalue("Matrikelnummer")
studiengang = form.getvalue("Studiengang")
semester = form.getvalue("Semester")
studienart = form.getvalue("studienart")
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
    <li>Stduiengang: {studiengang}</li>
    <li>Semester: {semester}</li>
    <li>Studienart: {studienart}</li>  
</ul>

</body>
</html>
""")
