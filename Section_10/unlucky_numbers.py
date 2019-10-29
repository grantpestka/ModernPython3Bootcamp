# state = ''
for x in range(0,20):
    if x == 4 or x == 13:
        state = 'unlucky'
    elif x%2 == 0:
        state = 'even'
    else:
        state = 'odd'
    print(f'{x} is {state}')