#This is the beginning of Lunkworld, a program to simulate that amazing city life. 
#Imports and initalizes packages 
import configparser
config = configparser.ConfigParser()
config.read('data.ini')
import os
def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):
    command = 'cls'
  os.system(command)
import time
#Imports other files in this program.
import store

#The worldMap function, it prints out the world map and asks the user on where they want to go.
def worldMap():
  energy = config.getint('playerData','energy')
  money = config.getint('playerData','money')
  clearConsole()
  print("Welcome to the world map!")
  print("When you enter anywhere, type in exit in an input prompt to leave!")
  print("Energy: ",energy)
  print("Money: ",money)
  print("")
  print("1 - Store")
  print("2 - Workplace")
  print("3 - House")
  print("4 - Club (Can only access if you have a VIP pass!)")
  print("5 - Close Lunkworld")
  inputVar = int(input("Just type in the corresponding number! "))
  if inputVar < 1 or inputVar > 5:
    while True:
      inputVar = int(input("Invalid input! Please try again. "))
      if inputVar >= 1 and inputVar <= 5:
        break
  print("Okay! Heading over now!")
  return(inputVar)
  
#logInCheck compares player input to their saved information. 
def logInCheck():
  global username
  global password
  check = True
  while check == True:
    userInputName = input("What's your username? ")
    userInputPass = input("What's your password? ")
    if userInputName != username or userInputPass != password:
      clearConsole()
      print("Sorry, that was the wrong username or password.")
    else:
      check = False
      clearConsole()
      print("Welcome back, "+username+".")
      
#This initalizes the file to include various sorts of information.
if not config.has_section("logIn"):
  config.add_section("logIn")
  config.set("logIn","previousInfo","False")
  config.set("logIn","userName","1")
  config.set("logIn","password","1")

if not config.has_section("playerData"):
  config.add_section("playerData")
  config.set("playerData","energy","100")
  config.set("playerData","money","50")

if not config.has_section("items"):
  config.add_section("items")
  config.set("items","VIP","False")
  config.set("items","apple","0")
  config.set("items","cheese","0")
  
  


#Grabs if the login exists, and then grabs the login information (username + password).
logIn = config.getboolean("logIn","previousInfo")
username = config.get("logIn","username")
password = config.get("logIn","password")
createInfo = False
if logIn == True:
  print("Welcome back to Lunkworld.")
if logIn == False:
    print("Welcome to Lunkworld, the last virtual game you'll ever need.")
    print("We see that you're brand new here, so let's go over a quick tutorial.")
    time.sleep(1)
    clearConsole()
    print("Soon you'll be introduced to the world map. From there, you can input information to access the buildings you want to vist. In the top left, you can see your username, and your energy. When your energy reaches 0 from doing activites, you'll have to retire for the night. In Lunkworld, you start off with 500 Lunkbucks, or LB for short. This is the only accepted currecy in this game! Have fun in Lunkworld!")
    asdkjasdkjasd = input("Press any key to continue.")
    clearConsole()
  #Simple logic to check if the login exists, and then creates new information if it doesn't exist. logInCheck() is called here. 
if logIn == False:
    createInfo = True
if createInfo == True:
    username = input("What do you want your username to be? ")
    username2 = username.lower()
    password = input("What do you want your password to be? ")
    config.set('logIn','username',username)
    password2 = input("Please input your password again for safety reasons. Capitalization matters! ")
    if password != password2:
      passCheck = False
      while passCheck == False:
        password2 = input("Please input the password again. Capitalization matters! ")
        if password == password2:
          passCheck = True
    config.set('logIn','password',password)
    config.set('logIn','previousInfo',"True")
    clearConsole()
    print("Log in created! Welcome in, "+username+".")
elif createInfo == False:
    logInCheck()
time.sleep(1.5)
clearConsole()
with open("data.ini","w") as configFile:
  config.write(configFile)
#HELP
whereGo = worldMap()
print(whereGo)