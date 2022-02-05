#These are just extra functions that I figured I would use alot.
def inputCheck(value1, value2, inputVal):
 if inputVal < value1 or inputVal > value2:
       while True:
         inputVal = int(input("Invalid input! Please try again. "))
         if inputVal >= value1 and inputVal <= value2:
            break