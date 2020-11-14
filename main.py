print("Start the Game")
num = int(input("Enter the number you want others to Guess: "))
number_of_guesses = 1
print("You have only 5 Guesses")

while number_of_guesses <= 5:
    guess_number = int(input("Guess the Number: "))
    if guess_number<num:
        print("Your Guess is less than the number")
    elif guess_number>num:
        print("Your Guess is more than the number")
    else:
        print("Right Guess!!!")
        print(f"You took {number_of_guesses} guesses.")
        break
    print("No. of guesses left: ",5-number_of_guesses)
    number_of_guesses = number_of_guesses + 1

if number_of_guesses>5:
    print("Sorry! You are out of Guesses.")
