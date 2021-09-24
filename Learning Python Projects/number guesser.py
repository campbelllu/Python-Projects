from math import *
import random
import sys

#make a number guessing game

#generate random number in a range
rando = random.randint(1,10)
counter = 0
guess = None
#print(rando)
#print guess a number, input is guessing
print("Guess the number I have chosen. \nIt is between 1 and 10, inclusively.")

while True:

  wrongFlag = False

  try:
    guess = input()
    #print("guess", guess)
    if str(guess.lower()) == "exit":
        print("1. You have chosen to quit guessing. Please leave the training center.")
        sys.exit() 
  #print("Thank you for making a guess.\n")
#compare guess to random
    while True:
      guess = int(guess)
      #if str(guess) == "exit":
       # print("You have chosen to quit guessing. Please leave the training center.")
        #sys.exit() 
      if guess < int(1) or guess > int(10):
        wrongFlag = True
      #print(wrongFlag)
        while wrongFlag == True:
          print("Unfortunately, your guess was outside of the accepted range. Please re-enter a number selection between 1 and 10, inclusively. ")
          counter += 1
          print("This was guess #", counter)
          guess = input()
          if int(guess) >= int(1) and int(guess) <= int(10):
          #wrongFlag == False
            break
          #else:
           # break
      #print("rando equals: ", rando)      
  #else:
      guess = int(guess)
      if guess == rando:
        print("Congratulations! You have guessed correctly. \nIt took you", counter, "attempts to guess correctly.\nProceed to the next test.")
        sys.exit() #break
      #print("guess before breaking", guess)
      if guess > rando:
        print("Inaccurate guess. You are guessing too high. Try again.")
        counter += 1
        print("This was guess #", counter)
        guess = input()
      if int(guess) < rando:
        print("Inaccurate guess. You are guessing too low. Try again.")
        counter += 1
        print("This was guess #", counter)
        guess = input()
       
  except ValueError:
    counter += 1
    #guess = input()
    print("This was guess #", counter)
    if str(guess.lower()) == "exit":
        print("2. You have chosen to quit guessing. Please leave the training center.")
        sys.exit()  
    else:    
      print("Your guess was not a number between 1 and 10, inclusively. Please make another guess, this time within the accepted parameters.")
    #guess = int(input())





#print("I have an item. " + item('a'))
