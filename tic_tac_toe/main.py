def hello():
    print ('Hello, let\'s play Tic Tac Toe!')

arr = [[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
       ['-','-','-','|','-','-','-','|','-','-','-'],
       [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
       ['-','-','-','|','-','-','-','|','-','-','-'],
       [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']]

def print_grid_example():
    arr[0][1] = 0
    arr[0][5] = 1
    arr[0][9] = 2
    arr[2][1] = 3
    arr[2][5] = 4
    arr[2][9] = 5
    arr[4][1] = 7
    arr[4][5] = 8
    arr[4][9] = 9
    for row in arr:
        print(' '.join([str(elem) for elem in row]))

def grid0_0():
    print (' x |   |   ')
    print ('---|---|---')
    print ('   |   |   ')
    print ('---|---|---')
    print ('   |   |   ')

def grid0_1():
    print ('   | x |   ')
    print ('---|---|---')
    print ('   |   |   ')
    print ('---|---|---')
    print ('   |   |   ')

def turn():
    print ('Please put your mark by entering position on the grid.')
    print ('For example, position 0.0 will put mark in the upper leftmost square.')
    x = input()
    if (x == 0.0):
        grid0_0()
    elif (x == 0.1):
        grid0_1()
    else:
        print ('other mark')


hello()
print_grid()
turn()