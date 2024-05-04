#!C:/Python35/python.exe
import cgi
from pymysql import *

class Formular_einlesen:
      def __init__(self):
         self.benutzername=""
         self.passwort=""
         self.birthday=""
         
      def db(self):
         con = connect(host="localhost", user="root", passwd="")
         cur = con.cursor()
         try:
            cur.execute("use abschlusprojektq2")
         except (Exception):
            cur.execute("create database abschlusprojektq2; use abschlusprojektq2")
         while 1:
               try:
                  cur.execute("INSERT INTO user (Benutzername, Passwort, Geburtstag) VALUES ('"+self.benutzername+"','"+self.passwort+"', '"+self.birthday+"')") 
                  con.commit() 
                  break
               except (Exception):
                  cur.execute("create table user (UserNr int not null auto_increment primary key, Benutzername text, Passwort text, Geburtstag date, BevorzugteMusikrichtungEins text, BevorzugteMusikrichtungZwei text)")
                  continue
         con.close()


      def fehler(self):
            print ("Content-Type: text/html")
            print()
            print('<!DOCTYPE html>\
                  <html>')
            print ('<head>\
               <title> Fehlermeldung </title>\
               <link rel="stylesheet" type="text/css" href="../Wilkommensseite.css"/>\
               </head>\
               <body>\
               <h1>Es ist ein Fehler aufgetreten:</h1>\
               <p>Bitte alle Felder ausf&uuml;llen!</p>\
               <p>\
               <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
               </p>\
               </body>\
               </html>')

      def auswertung(self):
            form = cgi.FieldStorage()
            if "Benutzername" in form:
                  self.benutzername = form["Benutzername"].value
            if "Passwort" in form:
                  self.passwort = form["Passwort"].value
            if "Geburtsjahr" in form:
                  self.birthday = form["Geburtsjahr"].value
            if  (self.benutzername=="" or self.passwort=="" or self.birthday==""):
               self.fehler()
            else:
               self.ausgabe()
      def ausgabe(self):
            self.db()
            print ("Content-Type: text/html")
            print()
            print('<!DOCTYPE html>\
                  <html>')
            print ('<head>\
                  <title>Anmeldung erfolgreich</title>\
                  <link rel="stylesheet" type="text/css" href="../Wilkommensseite.css"/>\
                  </head>\
                  <body>\
                  <h1>Herzlich willkommen, '+self.benutzername+', Sie sind jetzt registriert!</h1>\
                  <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
                  <a href="../FunktionsHTMl/LogIn_SignUp_Site.html"><button> Zur Anmeldung </button></a>\
                  </p>\
                  </body>\
                  </html>')
            

objekt=Formular_einlesen()
objekt.auswertung()
