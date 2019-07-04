import requests
import os

with open("Locations.txt","r") as file:

  lines = [i for i in file]

  file.close()

for x in range(20,40):

  url = "http://worldtimeapi.org/api/timezone/" + lines[x].strip() + ".txt"
  
  r = requests.get(url)
  
  with open("temp_file.txt","w+") as tempfile:

    tempfile.write(r.text)

  with open("temp_file.txt","r") as tempfile:

    temparr = [y for y in tempfile]

    tempfile.close()

  if temparr[2][21] == "1" and temparr[2][22] == "7":
    
    print("It is 5 0' clock PM in " + lines[x] + "ENJOY YOUR DRINKS RESPONSIBLY!!!!!!!!!!!!")
    
  else:
    
    print(lines[x] + ": it is not 5 o' clock here")
  
  del temparr

  os.remove("temp_file.txt")

del lines



