# for num in range(1,11):
#     art = "\U0001f600"
#     art = art * num
#     print(art)

max = 21    
for num in range(1,max,2):
    art = "\U0001f600"
    art = art * num
    space = int((max - num)/2)
    space = " " * space
    print(f'{space}{art}{space}')
  