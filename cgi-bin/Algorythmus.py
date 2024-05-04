from random import *
import cgi
from pymysql import *
import getCurrentValues
from webbrowser import *
import webbrowser

currentSong = getCurrentValues.getCurrentValues().currentSong()
currentSong=1

class SongRecomendation:
    def getSongsAtributes(self):
            con = connect(host="localhost", user="root", passwd="")
            cur = con.cursor()
            cur.execute("use abschlusprojektq2")
            
            #currentSongs attributes
            cur.execute("SELECT Interpret, Genre, Album FROM songs WHERE SongNr='%s'"%str(currentSong))
            res = cur.fetchall()
            self.songInterpret = res[0][0]
            self.songGenre = res[0][1]
            self.songAlbum = res[0][2]
            #print(self.songInterpret, self.songGenre, self.songAlbum)
            con.close()
            object.setSongsAccordance()


    def getGenreAccordance(self):
         self.similarGenres = []
         if self.songGenre == "HipHop" or "HipHop - Rap" or "HipHop - Reagie" or "RapRock":
              self.similarGenres.insert(self.i+1, "HipHop")
              self.similarGenres.insert(self.i+2, "HipHop - Reagie")
              self.similarGenres.insert(self.i+3, "HipHop - Rap")
              self.similarGenres.insert(self.i+4, "RapRock")
              self.i = self.i+4
         if self.songGenre == "Alternativ Rock" or "Rock" or "RapRock" or "Nu Metal" or "PopRock":
              self.i = len(self.similarGenres)
              self.similarGenres.insert(self.i+1, "Alternativ Rock")
              self.similarGenres.insert(self.i+2, "Rock")
              self.similarGenres.insert(self.i+3, "RapRock")
              self.similarGenres.insert(self.i+4, "Nu Metal")
              self.similarGenres.insert(self.i+5, "PopRock")
              self.i = self.i+5
         if self.songGenre == "Pop" or "PopRock":
              self.i = len(self.similarGenres)
              self.similarGenres.insert(self.i+1, "Pop")
              self.similarGenres.insert(self.i+1, "PopRock")
              self.i = self.i+2
         if self.songGenre == "Elektro" or "Phonk":
              self.i = len(self.similarGenres)
              self.similarGenres.insert(self.i+1, "Elektro")
              self.similarGenres.insert(self.i+2, "Phonk")
         return self.similarGenres

            
    def setSongsAccordance(self):
        self.i = 1
        k = 0
        j = 0
        songAcc1 = ""
        songAccordance1 = ""
        songAcc2 = ""
        songAccordance2 = ""
        self.SongListe = []
        songAccordance = 0

        con = connect(host="localhost", user="root", passwd="")
        cur = con.cursor()
        cur.execute("use abschlusprojektq2")
        cur.execute("SELECT COUNT(*) FROM songs")
        NumOfSong = cur.fetchall()[0][0]
        print(NumOfSong)
        while NumOfSong >= self.i:
            cur.execute("SELECT Interpret, Genre, Album FROM songs WHERE SongNr='%s'"%str(self.i))
            res = cur.fetchall()
            compairInterpret = res[0][0]
            compairGenre = res[0][1]
            compairAlbum = res[0][2]

            object.getGenreAccordance()

            if compairInterpret == self.songInterpret:
                 songAccordance = songAccordance+1
            while k <= len(self.similarGenres):
                 if compairGenre == self.similarGenres[k]:
                      songAccordance = songAccordance + 1
                      k = 0
                      break
                 k = k+1


            if compairAlbum == self.songAlbum:
                 songAccordance = songAccordance + 1

            if songAccordance > 0:
                 if songAcc1 == "":
                    songAcc1 = self.i
                    songAccordance1 = songAccordance
                 elif songAcc1 != "" and songAcc2 == "":
                    songAcc2 = self.i
                    songAccordance2 = songAccordance

                 while songAcc1 != "" and songAcc2 != "":
                      if songAccordance1 > songAccordance2:
                           self.SongListe.insert(j, songAcc1)
                           j = j+1
                           songAcc2 = ""
                           break

                      elif songAccordance1 < songAccordance2:
                           self.SongListe.insert(j, songAcc2)
                           j = j+1
                           songAcc1 = ""
                           break

                      else:
                           h = random()
                           if h == 0:
                                self.SongListe.insert(j, songAcc1)
                                songAcc2 = ""
                                break
                           elif h == 1: 
                                self.SongListe.insert(j, songAcc2)
                                songAcc1 = ""
                                break
                           else:
                                self.SongListe.insert(j, songAcc1)
                                songAcc2, songAcc1 = ""
                                break
            self.i = self.i+1

        object.setNextSong()

    def setNextSong(self):
         NumOfPossNextSongs = self.SongListe.length()
         i = randint(0, NumOfPossNextSongs)
         self.nextSong = self.SongListe[i]
         if self.nextSong == "" or self.nextSong == 0:
              self.nextSong = self.SongListe[0]

         self.settedSong = self.nextSong

         object.callNextSong()


    def callNextSong(self):
          form = cgi.FieldStorage()
          if "nextSong" in form:
               if self.settedSong == 1:
                    webbrowser.open("http://localhost:8888/Songs/Hurra, die Welt geht unter! - Lied.html") #Pfad
               elif self.settedSong == 2:
                    webbrowser.open("http://localhost:8888/Songs/Pizza.html") #Pfad
               elif self.settedSong == 3:
                    webbrowser.open("http://localhost:8888/Songs/Michael X.html") #Pfad
               elif self.settedSong == 4:
                    webbrowser.open("http://localhost:8888/Songs/Irgendeine Nummer.html") #Pfad     
               elif self.settedSong == 5:
                    webbrowser.open("http://localhost:8888/Songs/In the End.html") #Pfad     
               elif self.settedSong == 6:
                    webbrowser.open("http://localhost:8888/Songs/Sterben kannst du ueberall.html") #Pfad     
               elif self.settedSong == 7:
                    webbrowser.open("http://localhost:8888/Songs/Papercut.html") #Pfad              
               else:
                    webbrowser.open("http://localhost:8888/Songs/Songs/Fall Out Boy - Immortals")
          else:
               webbrowser.open("http://localhost:8888/Songs/Songs/Papercut")



object=SongRecomendation()
object.getSongsAtributes()
