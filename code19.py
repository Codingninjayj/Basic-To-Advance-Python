#Exesise 3:Guessing Game
# In a guessing game: A while loop can be used to keep track of the number of guesses the user has made and to continue the game until the user guesses the correct answer. For example, the following code shows a while loop that is used to keep track of the number of guesses the user has made in a guessing game:

guess=0
while(guess<10):
    guess=int(input("Enter the number Between 1 to 10:"))
    if(guess==5):
        print("Your correct!!!!!")
        break
    elif(guess==6):
        print("Your Corret!!!")
    else:
        guess +=1 #This statement is used to retrun to the starting point
        print("your Worng !Try Again")
