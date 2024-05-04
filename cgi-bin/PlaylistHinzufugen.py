from pymysql import *
import pymysql
import cgi
import getCurrentValues


currentSong = getCurrentValues.getCurrentValues().currentSong()
currentAccount = getCurrentValues.getCurrentValues().currentAccount()

con = connect(host="localhost", user="root", passwd="")
cur = con.cursor
cur.execute("use abschlussprojektq2")

cur.execute("SELECT PlaylistEintrag FROM playlist WHERE SongNr='" +currentSong+ "' AND AccountNr='"+currentAccount"'")
check4Song = cur.fatchall()[0][0]
if check4Song != "" or 0:   #Entfernen
    cur.execute("DELETE FROM playlist WHERE Playlisteintrag='"+check4Song+"' AND AccountNR='"+currentAccount"'")

else: 						#Hinzufügen
	cur.execute("INSERT INTO playlist (SongNr, AccountNr) VALUES ('"+currentSong+"', '"+currentAccount+"')")