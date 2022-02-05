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
import QOL
import store
import fileMod

#The worldMap function, it prints out the world map and asks the user on where they want to go.
def worldMap():
  energy = 0#config.getint('playerData','energy')
  money = 0#config.getint('playerData','money')
  clearConsole()
  print("Welcome to the world map!")
  print("When you enter anywhere, type in 505 at an input prompt to leave!")
  print("Energy: ",energy)
  print("Money: ",money)
  print("")
  print("1 - Store")
  print("2 - Workplace")
  print("3 - House")
  print("4 - Club (Can only access if you have a VIP pass!)")
  print("5 - Check your inventory")
  print("6 - Close Lunkworld")

  inputVar = int(input("Just type in the corresponding number! "))
  QOL.inputCheck(1, 5, inputVar)
  print("Okay! Heading over now!")
  return(inputVar)

      
#This initalizes the file to include various sorts of information.
fileMod.fileInt()
money = 50#config.getint('playerData','money')

time.sleep(1.5)
clearConsole()

#Logic to control the world map
whereGo = worldMap()

if whereGo == 1:
    store.storeFront(money)
    #config.set("items",'apple','1')

    #print("apple")

