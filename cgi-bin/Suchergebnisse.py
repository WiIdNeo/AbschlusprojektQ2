# search_songs.py

import mysql.connector
import cgi
import cgitb
cgitb.enable()

# Verbindung zur Datenbank herstellen
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="abschlusprojektq2"
)

cursor = db.cursor()

# Benutzereingabe aus dem HTML-Formular verarbeiten
form = cgi.FieldStorage()
search_query = form.getvalue("query")

# SQL-Abfrage ausführen
query = f"""
    SELECT SongNr, Titel, Album, Interpret
    FROM songs
    WHERE Titel LIKE '%{search_query}%'
       OR Album LIKE '%{search_query}%'
       OR Interpret LIKE '%{search_query}%'
"""

cursor.execute(query)
results = cursor.fetchall()

# HTML-Tabelle erstellen
html_table = "<table>"
html_table += "<tr><th>SongNr</th><th>Titel</th><th>Album</th><th>Interpret</th></tr>"
for row in results:
    html_table += f"""
        <tr>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
            <td>{row[3]}</td>
            <td><a href=\"../Songs/song{row[0]}.html\">Zum Song</a></td>
        </tr>
    """
html_table += "</table>"

# HTML-Seite generieren
print("Content-Type: text/html;charset=utf-8")
print()
print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Suchergebnisse</title>
</head>
<body>
    <h1>Suchergebnisse für: {search_query}</h1>
    {html_table}
</body>
</html>
""")

# Verbindung schließen
db.close()