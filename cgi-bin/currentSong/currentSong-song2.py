import cgi
import cgitb

cgitb.enable()  
currentSong = 2

# Specify the file path
file_path = "currentSong.txt"

# Write the value to the file
with open(file_path, "w") as file:
    file.write(str(currentSong))

print(f"Value {currentSong} written to {file_path}")