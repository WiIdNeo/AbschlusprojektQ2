from pymysql import *
import pymysql
import cgi
import getCurrentValues


currentSong = getCurrentValues.getCurrentValues().currentSong()
currentAccount = getCurrentValues.getCurrentValues().currentAccount()

con = connect(host="localhost", user="root", passwd="")
cur = con.cursor
cur.execute("use abschlussprojektq2")

cur.execute("SELECT FavoritenNr FROM favoriten WHERE SongNr='" +currentSong+ "' AND AccountNr='"+currentAccount"'")
check4Song = cur.fatchall()[0][0]
if check4Song != "" or 0:   #Entfernen
    cur.execute("DELETE FROM favoriten WHERE FavoritenNr='"+check4Song+"' AND AccountNr='"+currentAccount"'")

else: 						#Hinzufügen
	cur.execute("INSERT INTO favoriten (SongNr, AccountNr) VALUES ('"+currentSong+"', '"+currentAccount+"')")


