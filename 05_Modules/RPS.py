from random import choice

# 1. Ask for player name
player_name = input('Introdu numele: ')
# 2. Greet and show playing options
print('Welcome: `Rock - Paper - Scissors` ')

full_names={'r' : 'Rock', 'p' : 'Paper', 's' : 'Scissors'}

game_on = True
while game_on:

    # 3. Player is asked to make a choice (read from the console)
    comp_choice = None
    user_choice = None
    while comp_choice == user_choice:
        user_choice = input('Choose from: "R/P/S"').lower()
        optiuni = ['r', 'p', 's']
        while user_choice not in optiuni:
            user_choice = input('Choose from: "R/P/S"').lower()
        # 4. Computer makes a random choice
        print('Egalitate se alege din nou! \n')
        comp_choice = choice(optiuni)
        print(comp_choice)
        # 5. If computer makes the same choice, play again
    print(f'{player_name}\'s choice was: {full_names[user_choice]}')
    print(f'The computer\'s choice was: {full_names[comp_choice]}')

    if user_choice == 'r':
        if comp_choice == 'p':
            print('The computer won :(')
        else:
            print(f'{player_name} won :)')
    elif user_choice == 'p':
        if comp_choice == 's':
            print('The computer won :(')
        else:
            print(f'{player_name} won :)')
    else:
        if comp_choice == 'r':
            print('The computer won :(')
        else:
            print(f'{player_name} won :)')
    game_status = input('Do you want to play again? y/n ')
    while game_status not in 'yn':
        game_status = input('Do you want to play again? y/n ')
    if game_status != 'y':
        game_on = False

# 6. If not, show the result
# 7. Ask player if he/she wants to play again
# 8. Game stops when the player decides not to play again
# de pus While: