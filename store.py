#The Lunkworld Store
#Import packages
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
import QOL

#Money check is self explanitory, it compares the amount of money the player has to the cost of the thing they want to buy
def moneyCheck(money,itemCost):
    if(money >= itemCost):
        return(True)
    else:
        return(False)

#Storefront, most of the code relevant to the store
def storeFront(money):
  print("Howdy partner, welcome to the Lunkworld general store. What can I get for you?")
  print("1 - Apple ($5) - Restores 5 energy")
  print("2 - Cheese ($20) - Restores all of your energy")
  print("3 - Helmet ($75) - Makes you more qualified at your job!")
  print("4 - Fishing Rod ($125) - Allows you to fish for goodies")
  print("5 - VIP Pass ($500) - Allows you to enter the club")
  print("6 - Terence Statue ($1000) - Shows true dedication through a funky rap!")
  storeItem = int(input("Just enter the number of the item you want. "))

  while money >= 0:
    if (storeItem == 1):
        buy = moneyCheck(money, 5)
        if buy == True:
            apple = config.getint('items','apple')
            print(money)
            apple += 1
            config.set('items','apple','2')

            cash = config.getint('playerData', 'money')
            cash -= 5
            config.set('playerData','money',str(cash))
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
        break
    
    if (storeItem == 3):
        buy = moneyCheck(money, 75)
        if buy == True:
            helmet = config.getint('items','helmet')
            helmet = True
            config.set('items','helmet',str(helmet))
            break
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
            break
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
        break