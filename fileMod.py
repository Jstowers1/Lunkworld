import configparser
import time
import QOL
config = configparser.ConfigParser()
config.read('data.ini')
import os
def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):
    command = 'cls'
  os.system(command)

#Money check is self explanitory, it compares the amount of money the player has to the cost of the thing they want to buy
def moneyCheck(money,itemCost):
    if(money >= itemCost):
        return(True)
    else:
        return(False)

#logInCheck compares player input to their saved information. 
def logInCheck():
  username = config.get("logIn","username")
  password = config.get("logIn","password")
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

def fileInt():
    config.read('data.ini')
    if not config.has_section("logIn"):
      config.add_section("logIn") # creates logIn
      config.set("logIn","previousInfo","False") # provides attributes to logIn
      config.set("logIn","userName","1")
      config.set("logIn","password","1")
    if not config.has_section("playerData"):
      config.add_section("playerData")
      config.set("playerData","energy","100")
      config.set("playerData","money","50")
    if not config.has_section("items"):
      config.add_section("items")
      config.set("items","VIP","False")
      config.set("items","helmet","False")
      config.set("items","fishingRod","False")
      config.set("items","apple","0")
      config.set("items","cheese","0")
      config.set("items","terence","0")
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
    with open("data.ini","w") as configFile:
      config.write(configFile)

def storePurchase(money, storeItem):
    config = configparser.ConfigParser()
    config.read('data.ini')
    if (storeItem == 1):
        buy = moneyCheck(money, 5)
        if buy == True:
            apple = config.getint('items','apple')
            print(money)
            print(apple)
            apple += 1
            config.set('items','apple','2')
            money = money - 5
            config.set('playerData','money',str(money))
            print("apple")
            return
        else:
            print("You don't have enough money for this purchase!")

    if (storeItem == 2):
        buy = moneyCheck(money, 20)
        if buy == True:
            cheese = config.getint('items','cheese')
            cheese += 1
            config.set('items','cheese',str(cheese))
        else:
            print("You don't have enough money for this purchase!")
    
    if (storeItem == 3):
        buy = moneyCheck(money, 75)
        if buy == True:
            helmet = config.getint('items','helmet')
            helmet = True
            config.set('items','helmet',str(helmet))
        else:
            print("You don't have enough money for this purchase!")

    if (storeItem == 4):
        buy = moneyCheck(money, 125)
        if buy == True:
            fishingrod = config.getint('items','fishingrod')
            fishingrod += 1
            config.set('items','fishingrod',str(fishingrod))
        else:
            print("You don't have enough money for this purchase!")

    if (storeItem == 5):
        buy = moneyCheck(money, 500)
        if buy == True:
            vip = config.getint('items','vip')
            vip = True
            config.set('items','vip',str(vip))
        else:
            print("You don't have enough money for this purchase!")

    if (storeItem == 6):
        buy = moneyCheck(money, 1000)
        if buy == True:
            terence = config.getint('items','terence')
            terence += 1
            config.set('items','terence',str(terence))
        else:
            print("You don't have enough money for this purchase!")
   
    if (storeItem == 505):
        print("It was nice to have you at our shop!")
    with open("data.ini","w") as configFile:
      config.write(configFile)