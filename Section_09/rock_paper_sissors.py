print('Rock...')
print('Paper...')
print('Sissors...')

player1 = input('player 1, make your move: ')
print('*** no cheating !!! \n\n' * 20)
player2 = input('player 2, make your move: ')

winner = 'something went wrong. No one'

if player1 == player2:
    winner = 'Its a tie. No one'
elif player1 == 'rock':
    if player2 == 'paper':
        winner = 'Player2'
    elif player2 == 'sissors':
        winner = 'Player1'
elif player1 == 'paper':
    if player2 == 'sissors':
        winner = 'Player2'
    elif player2 == 'rock':
        winner = 'Player1'
elif player1 == 'sissors':
    if player2 == 'rock':
        winner = 'Player2'
    elif player2 == 'paper':
        winner = 'Player1'
print(f'{winner} wins')