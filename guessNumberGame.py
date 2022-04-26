# This is just a simple number guessing game
# Nothing serious, just for fun
# Created by Chaby Manow
import random

print("What is your name?")
playerName = input()

print("Hello " + playerName +"! I am guessing a number between 1 and 20.\n Can you guess my number?")
secretNumber = random.randint(1, 20)

for guesses in range(1, 7):
 print("Please guess a number!")
 playerGuess = int(input())
 
 if playerGuess > secretNumber:
     print("Your number is too high! Try a lower number1")
 elif playerGuess < secretNumber:
     print("Your number is too low! Try a bigger number!")
 else:
     break
    
if playerGuess == secretNumber:
    print("Nice job " +playerName+ "! You guessed my number!")
    end = input()
else:
    print("It is too much try " +playerName+"! My secret number was: " +str(secretNumber))
