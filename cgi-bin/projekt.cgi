#!/usr/bin/python3

import cgi


form = cgi.FieldStorage()
matrikelnummer = form.getvalue("Matrikelnummer")
studiengang = form.getvalue("Studiengang")
semester = form.getvalue("Semester")
studienart = form.getvalue("Studienart")

print("Content-type: text/html")
print()

print(f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
        <meta name="viewport"
          content="width=device-width, initial-scale=1.0">
    <title>Ausgabe</title>
        <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css">

    <link rel="stylesheet"
          href="../Betriebssysteme-Webcomputing-Semesterabgabe/css/main.css">
</head>
<body>

<div class="container mt-5">

    <div class="col-md-6 mx-auto">

        <div class="card p-4 shadow">

            <h1 class="text-center mb-4">
                Eingegebene Daten
            </h1>

            <ul class="list-group">

                <li class="list-group-item">
                    Matrikelnummer: {matrikelnummer}
                </li>

                <li class="list-group-item">
                    Studiengang: {studiengang}
                </li>

                <li class="list-group-item">
                    Semester: {semester}
                </li>

                <li class="list-group-item">
                    Studienart: {studienart}
                </li>

            </ul>
	</div>

<ul class="list-group list-group-horizontal-xl flex-fill">
  <li class="list-group-item">Cras justo odio</li>
  <li class="list-group-item">Dapibus ac facilisis in</li>
  <li class="list-group-item">Morbi leo risus</li>
 <li class="list-group-item">Morbi leo risus</li>
 <li class="list-group-item">Morbi leo risus</li>
</ul>
    </div>
</div>
<footer class="bg-body-tertiary text-center mt-auto">

    <div class="text-center p-3"
         style="background-color: rgba(0, 0, 0, 0.05);">

        GitHub Paul Sohnrey & Vanessa Folte:

        <a class="text-reset fw-bold"
           href="https://github.com/RentoxYT/Betriebssysteme-Webcomputing-Semesterabgabe">

           Repository

        </a>

    </div>

</footer>
</body>
</html>
""")
