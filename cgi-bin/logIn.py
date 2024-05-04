#!C:/Python35/python.exe
import cgi
from pymysql import *
import cgitb
currentAccount=0

class Formular_einlesen:
      def __init__(self):
         self.benutzername=""
         self.password=""
         self.checkAccount=""
         self.currentAccount = ""
         self.liste=[]
         
      def db(self):
         con = connect(host="localhost", user="root", passwd="")                                             #Verbinden mit der Datenbank
         cur = con.cursor()
         cur.execute("use abschlusprojektq2")

         cur.execute("SELECT Passwort, UserNr FROM user WHERE Benutzername='"+self.benutzername+"'")         #Auslesen des Passworts/Nutzernamens mit dem eingegebenen Wert
         res = cur.fetchall()   
         for row in res:
                  self.liste.append(row)
         try:
               self.checkAccount = self.liste[0][0]
               self.currentAccount = str(self.liste[0][1])
         except(Exception):                                                      
               self.fehler()
         con.close()
         
         if self.checkAccount == self.password:                                                               #
               self.ausgabe()
               cgitb.enable()  
               file_path = "../currentAccount.txt"

               with open(file_path, "w") as file:
                  file.write(str(self.currentAccount))

         else:
               self.fehler()
                        
      
              
      
            
      



      def auswertung(self):
            form = cgi.FieldStorage()
            if "Benutzername" in form:
                  self.benutzername = form["Benutzername"].value
            if "password" in form:
                  self.password = form["password"].value
            
            self.db()
            



      def ausgabe(self):
            print ("Content-Type: text/html")
            print()
            print('<!DOCTYPE html>\
                  <html>')
            print ('<head>\
                  <title>Anmeldung erfolgreich</title>\
                  <link rel="stylesheet" type="text/css" href="../Wilkommensseite.css"/>\
                  </head>\
                  <body>\
                  <h1>Herzlich willkommen, '+self.benutzername+', AccountNr: '+self.currentAccount+' !</h1>\
                  <p><div class = "text">Sie sind jetzt angemeldet!\
                  <p>\
                  <a href="../FunktionsHTMl/Menü.html"> <button> <p> Main Menue </p> </button> </a>\
                  <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
                  </p>\
                  </body>\
                  </html>')
      
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
               <p>Accountdaten stimmen nicht überein!</p>\
               <p>\
               <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
               </p>\
               </body>\
               </html>')
            

objekt=Formular_einlesen()
objekt.auswertung()
