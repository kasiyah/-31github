def hello():
    print ('Hello, let\'s play Tic Tac Toe!')

def print_grid():
    print ('   |   |   ')
    print ('---|---|---')
    print ('   |   |   ')
    print ('---|---|---')
    print ('   |   |   ')

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