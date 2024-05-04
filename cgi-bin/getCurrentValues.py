


class getCurrentValues:
    def currentAccount():
        x = x

    def currentSong(self):
        folder_path = "/currentSong"
        file_name = "current_song.txt"

        file_path = f"{folder_path}/{file_name}"

        try:
            with open(file_path, "r") as file:
                currentSongVa = int(file.read())
                print(f"Read value {currentSongVa} from {file_path}")
        except FileNotFoundError:
            currentSongVa = 0
            
        return currentSongVa


    def currentAccount(self):
        folder_path = "./cgi-bin"
        file_name = "currentAccount.txt"

        file_path = f"{folder_path}/{file_name}"

        try:
            with open(file_path, "r") as file:
                currentAccountVa = int(file.read())
                print(f"Read value {currentAccountVa} from {file_path}")
        except FileNotFoundError:
            currentAccountVa = 0
            
        return currentAccountVa


object=getCurrentValues()
object.currentAccount()
object.currentSong()

