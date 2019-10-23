import random

print('Rock...')
print('Paper...')
print('Sissors...')

player1 = input('Make your move: ').lower().strip()
player2 = random.randint(0,2)
winner = 'something went wrong. No one'

if player2 == 0:
    player2 = 'rock'
elif player2 == 1:
    player2 = 'paper'
else:
    player2 = 'sissors'



if player1 == player2:
    winner = 'Its a tie. No one'
elif player1 == 'rock':
    if player2 == 'paper':
        winner = 'Computer'
    elif player2 == 'sissors':
        winner = 'Player'
elif player1 == 'paper':
    if player2 == 'sissors':
        winner = 'Computer'
    elif player2 == 'rock':
        winner = 'Player'
elif player1 == 'sissors':
    if player2 == 'rock':
        winner = 'Computer'
    elif player2 == 'paper':
        winner = 'Player'
print(f'Computer\'s move: {player2}'
)
print(f'{winner} wins')