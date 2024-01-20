import random

options = ("Rock", "Paper", "Scissors") 
score = 0
press = ("Yes", "No")
press = input("Start the Game Yes or No: ")

while press.lower() == "yes":
    user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
    computer_choice = random.choice(options).capitalize()

    print("Your Choice:", user_choice)
    print("Computer Choice:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        print("You win!")
        score += 1
        print("Your Score: " ,score) 
    else:
        print("Computer wins!")
        

    press = input("Play again Yes or No: ")
    if press.lower() == "no":
        break

print("Your Score: " ,score) 
print("Game over")