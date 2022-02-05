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

def storeFront(money):
  print("Howdy partner, welcome to the Lunkworld general store. What can I get for you?")
  print("1 - Apple ($5) - Restores 5 energy")
  print("2 - Cheese (#20) - Restores all of your energy")
  print("3 - Helmet ($75) - Makes you more qualified at your job!")
  print("4 - Fishing Rod ($125) - Allows you to fish for goodies")
  print("5 - VIP Pass ($500) - Allows you to enter the club")
  print("6 - terence statue ($1000) - Shows true dedication through a funky rap!")