import random

player_score = 0
computer_score = 0
winning_score = 3

while player_score < winning_score and computer_score < winning_score:
    print(f'Player Score: {player_score} Computer Score: {computer_score}')
    print('Rock...')
    print('Paper...')
    print('Sissors...')

    player1 = input('Make your move: ').lower().strip()
    player2 = random.randint(0,2)
    winner = 'something went wrong. No one'

    # determin computer move
    if player2 == 0:
        player2 = 'rock'
    elif player2 == 1:
        player2 = 'paper'
    else:
        player2 = 'sissors'

    # determin winner
    if player1 == player2:
        winner = 'Its a tie. No one'
    elif player1 == 'rock':
        if player2 == 'paper':
            winner = 'Computer'
            computer_score += 1
        elif player2 == 'sissors':
            winner = 'Player'
            player_score += 1
    elif player1 == 'paper':
        if player2 == 'sissors':
            winner = 'Computer'
            computer_score += 1
        elif player2 == 'rock':
            winner = 'Player'
            player_score += 1
    elif player1 == 'sissors':
        if player2 == 'rock':
            winner = 'Computer'
            computer_score += 1
        elif player2 == 'paper':
            winner = 'Player'
            player_score += 1
    print(f'Computer\'s move: {player2}'
    )
    print(f'{winner} wins \n')

# determine series winner
print(f'Final Score:: Player: {player_score} Computer: {computer_score}')
if player_score > computer_score:
    print('Player WINS')
else:
    print('Computer WINS')