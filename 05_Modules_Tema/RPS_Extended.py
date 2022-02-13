from random import choice

#Define a function which determines the outcome of the game
def rpslsp(uc, cc):
    if uc == 'r':
        if cc == 'p':
            winner = 'comp'
        elif cc == 's':
            winner = 'usr'
        elif cc == 'l':
            winner = 'usr'
        else: winner = 'comp'
    elif uc == 'p':
        if cc == 'r':
            winner = 'usr'
        elif cc == 's':
            winner = 'comp'
        elif cc == 'l':
            winner = 'comp'
        else: winner = 'usr'
    elif uc == 's':
        if cc == 'r':
            winner = 'comp'
        elif cc == 'p':
            winner = 'usr'
        elif cc == 'l':
            winner = 'usr'
        else: winner = 'comp'
    elif uc == 'l':
        if cc == 'r':
            winner = 'comp'
        elif cc == 'p':
            winner = 'usr'
        elif cc == 's':
            winner = 'comp'
        else: winner = 'usr'
    else:
        if cc == 'r':
            winner = 'usr'
        elif cc == 'p':
            winner = 'comp'
        elif cc == 's':
            winner = 'usr'
        else:
            winner = 'comp'
    return winner

# 1. Ask for player name
player_name = input('Introdu numele tau: ')
# 2. Greet and show playing options
print('Welcome to `Rock - Paper - Scissors - Lizard - Spock` ')

full_names={'r' : 'Rock', 'p' : 'Paper', 's' : 'Scissors', 'l' : 'Lizard', 'sp': 'Spock'}

game_on = True
while game_on:

    # 3. Player is asked to make a choice (read from the console)
    comp_choice = None
    user_choice = None
    while comp_choice == user_choice:
        user_choice = input('Choose from: "R/P/S/L/SP"').lower()
        optiuni = ['r', 'p', 's', 'l', 'sp']
        while user_choice not in optiuni:
            user_choice = input('Please choose a valid option from: "R/P/S/L/SP"').lower()
        # 4. Computer makes a random choice
        print('Egalitate se alege din nou! \n')
        comp_choice = choice(optiuni)
        # 5. If computer makes the same choice, play again
    print(f'{player_name}\'s choice was: {full_names[user_choice]}')
    print(f'The computer\'s choice was: {full_names[comp_choice]}')

    winner_name = rpslsp(user_choice, comp_choice)
    if winner_name == 'usr':
        print(f'{player_name} won :)')
    else:
        print('The computer won :(')
    game_status = input('Do you want to play again? y/n ')
    while game_status not in 'yn':
        game_status = input('Do you want to play again? y/n ')
    if game_status != 'y':
        game_on = False

# 6. If not, show the result
# 7. Ask player if he/she wants to play again
# 8. Game stops when the player decides not to play again
# de pus While: