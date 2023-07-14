#generate random number and see how many times the user gets it 
import random


top_of_range=input("Type a number: ")



if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <=0:
        print('Please type a number larger than 0')
        quit()
else :
    print('please tyoe a number next time')
    quit()


random_number = random.randint(0,top_of_range)# have to include top and bottom of range
guesses =0

while True:
    guesses +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)#user inputs a number that gets recognized as a string , we convert it to number in the next statement 
    else:
        print('Please type a number next time. ')
        continue #brings us back to the top of this loop 
    if user_guess == random_number:
        print("You got it!")
        break #if we add this , then the loop breaks after the correct option is selected
    elif user_guess > random_number:
        print("you were above the number!")
    else:
        print("you were below the number")

print("You got it in ",guesses,"guesses") #here print automatically converts the number to string

    
