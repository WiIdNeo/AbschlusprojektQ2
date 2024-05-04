
from pymysql import *
from datetime import datetime
import getCurrentValues

class Account:
    def handleRequest(self):
        self.AccountNum = getCurrentValues.getCurrentValues().currentAccount()
        self.username=""
        self.birthday=""
        self.favsong= ""
        self.favband= ""
        self.favoriteGenre=""

        con = connect(host="localhost", user="root", passwd="")
        cur = con.cursor()
        cur.execute("use abschlusprojektq2")
        # print("Content-Type: text/html")
        # print("")
        # print("SELECT favSong, favBand, favGenre, Geburtstag, Benutzername FROM user WHERE UserNr=" +str(self.AccountNum))
        # return
        cur.execute("SELECT favSong, favBand, favGenre, Geburtstag, Benutzername FROM user WHERE UserNr=" +str(self.AccountNum))
        res = cur.fetchall()
        # print("Content-Type: application/json")
        # print("")
        # print(res)
        # return
        self.favsong = res[0][0]
        self.favband = res[0][1]
        self.favoriteGenre = res[0][2]
        self.birthday = res[0][3]
        self.username = res[0][4]

        con.close()

        self.Account_ausgeben()



    def Account_ausgeben(self):
            print ("Content-Type: text/html")
            print()
            print('<!DOCTYPE html>\
                <html>')
            print ('<head>\
            <title> Fehlermeldung </title>\
            <link rel="stylesheet" type="text/css" href="../Account.css"/>\
            </head>\
            <body>\
                   <div>\
                    <table>\
                        <tr>\
                            <th>\
                                <p id="textsettings"> User name</p>\
                            </th>\
                            <th>\
                                <p id="textsettings"> '+self.username+'</p>\
                            </th>\
                        </tr>\
                        <tr>\
                            <th>\
                                <p id="textsettings"> Account Nummer</p>\
                            </th>\
                            <th>\
                                <p id="textsettings"> '+str(self.AccountNum)+'</p>\
                            </th>\
                        </tr>\
                        <tr>\
                            <th>\
                                <p id="textsettings"> Geburtstag</p>\
                            </th>\
                            <th>\
                                <p id="textsettings"> '+self.birthday.strftime("%d.%m.%Y")+'</p>\
                            </th>\
                        </tr>\
                        <tr>\
                            <th>\
                                <p id="textsettings"> Lieblingslied</p>\
                            </th>\
                            <th>\
                                <p id="textsettings"> '+self.favsong+'</p>\
                            </th>\
                        </tr>\
                        <tr>\
                            <th>\
                                <p id="textsettings"> Lieblingsband</p>\
                            </th>\
                            <th>\
                                <p id="textsettings"> '+self.favband+'</p>\
                            </th>\
                        </tr>\
                        <tr>\
                            <th>\
                                <p id="textsettings"> Lieblingsgenre</p>\
                            </th>\
                            <th>\
                                <p id="textsettings"> '+self.favoriteGenre+'</p>\
                            </th>\
                        </tr>\
                    </table>\
                </div>\
            </body>\
            </html>')
            
                
object=Account()
object.handleRequest()
