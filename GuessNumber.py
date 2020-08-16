#Exercise 3

print("Welcome To Number Guessing Game")
print("You have 10 attempt to guess the number")
num=20
no_of_guesses=0
while(True):
    no_of_guesses=no_of_guesses+1
    if no_of_guesses>10:
        print("No of guesses exceeds\n")
        print("Game Over\n")
        break
    print("Enter any number:", end= " ")
    user_input= int(input())
    if user_input>num:
        print("You entered greater number\n")
    elif user_input<num:
        print("You entered samller number\n")
    else:
        print("Congrats You Guessed The Correct Number\n")
        print(no_of_guesses, "no.of guesses he took to finish.")
        break