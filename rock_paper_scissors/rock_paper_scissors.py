import random as rd

print("Welcome to my Rock Paper Scissors Game!! :)\n\n")

ties = 0
wins = 0
losses = 0

def rock_paper_scissors(choice):
    # to be able to increment global variables, they need to be called as local
    global ties
    global wins
    global losses

    # selection of choices for CPU
    select = ['Rock', 'Paper', 'Scissors']
    cpu_choice = rd.choice(select)

    # conditions to apply rules of the game based on the choices made
    if cpu_choice == choice:
        ties += 1
        return f"You chose {choice}, CPU chose {cpu_choice}. It's a tie!"
    
    elif cpu_choice == 'Rock' and choice == 'Paper':
        wins += 1
        return f"You chose {choice}, CPU chose {cpu_choice}. You Won!"
    
    elif cpu_choice == 'Rock' and choice == 'Scissors':
        losses += 1
        return f"You chose {choice}, CPU chose {cpu_choice}. You lost!"
    
    elif cpu_choice == 'Paper' and choice == 'Rock':
        losses += 1
        return f"You chose {choice}, CPU chose {cpu_choice}. You Lost!"
    
    elif cpu_choice == 'Paper' and choice == 'Scissors':
        wins += 1
        return f"You chose {choice}, CPU chose {cpu_choice}. You Won!"
    
    elif cpu_choice == 'Scissors' and choice == 'Rock':
        wins += 1
        return f"You chose {choice}, CPU chose {cpu_choice}. You Won!"
    
    elif cpu_choice == 'Scissors' and choice == 'Paper':
        losses += 1
        return f"You chose {choice}, CPU chose {cpu_choice}. You Lost!"
    
    # this acts as a error handler for situations of mispelling or other 
    else :
        print("Please select between Rock, Paper or Scissors only. (check your spelling)")
    

# lets loop the game to continue until stated otherwise 
while True:

    user_choice = input("Please enter either Rock, Paper or Scissors : ").capitalize()
    outcome = rock_paper_scissors(user_choice)

    print(outcome)
    
    terminate = input("Go again? (Y/N) : ").upper()
    
    if terminate == 'N':
        print(f"Game stats: \nWon: {wins} \nLosses: {losses} \nTies: {ties} \nTotal games: {wins + losses + ties}")
        break
    
    elif terminate == 'Y':
        continue

    # error handling if user doesn't press especifically Y or N, it assumes as a yes and continues
    else :
        print("Although you didn't select Y or N, I'll take that as a Yes.\nGood luck! :)") 
