import random
options = ["r", "p", "s"]
print("Welcome to Sarah's rock, paper and scissors game!")
playing = input("Do you want to play?\nInput 'y' for 'yes' and 'n' for 'no': ").lower()

while True:
    if playing == "y":
        print("Let's Play!")

        print("'r'is for 'rock'\n'p' is for 'paper'\n's' is for 'scissors'")
        user_input = input("Pick an option between r, p and s: ").lower()
        if user_input not in ["r", "p", "s"]:
            print("invalid option")
            continue
        # setting up the computer choice
        random_number = random.randint(0, 2)
        # rock:0 paper:1 scissors:2
        computer_pick = options[random_number]
        #printing out players choice
        print("You picked", user_input + ".")
        print("Computer picked", computer_pick + ".")
        if user_input == computer_pick:
            print("It's a tie. Play again")
            continue
        # losing conditions
        if user_input == "r" and computer_pick == "p":
            print("Paper covers rock. Computer wins!")
            break
        if user_input == "p" and computer_pick == "s":
            print("Scissors cuts paper. Computer wins!")
            break
        if user_input == "s" and computer_pick == "r":
            print("Rock breaks scissors. Computer wins!")
            break
        # winning conditions
        if user_input == "r" and computer_pick == "s":
            print("Rock breaks scissors. You win!")
            break
        if user_input == "s" and computer_pick == "p":
            print("Scissors cuts paper. You win!")
            break
        if user_input == "p" and computer_pick == "r":
            print("Paper covers rock. You win!")
            break

    elif playing == "n":
        print("Okay, Goodbye.")
        break
    else:
        print("Sorry, your input isn't recognized.")
        break