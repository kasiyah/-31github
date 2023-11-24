def hello():
    print ('Hello, let\'s play Tic Tac Toe!')

arr = [[' ','x',' ','|',' ',' ',' ','|',' ',' ',' '],
       ['-','-','-','|','-','-','-','|','-','-','-'],
       [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
       ['-','-','-','|','-','-','-','|','-','-','-'],
       [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']]

def print_grid_example():
    arr1 = [[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
       ['-','-','-','|','-','-','-','|','-','-','-'],
       [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
       ['-','-','-','|','-','-','-','|','-','-','-'],
       [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']]
    arr1[0][1] = 0
    arr1[0][5] = 1
    arr1[0][9] = 2
    arr1[2][1] = 3
    arr1[2][5] = 4
    arr1[2][9] = 5
    arr1[4][1] = 6
    arr1[4][5] = 7
    arr1[4][9] = 8
    for row in arr1:
        print(' '.join([str(elem) for elem in row]))

def update_grid(j,k):
    for row in arr:
        arr[j][k] = 'x'
        
def print_grid():
    for row in arr:
        print(' '.join([str(elem) for elem in row]))

def turn():
    print ('Please put your mark by entering position on the grid as shown in example above.')

    x = input()
    if (x == "0" and arr[0][1] == ' '):
        update_grid(0,1)
    elif (x == "1"):
        update_grid(0,5)
    elif (x == 2):
        update_grid(0,9)
    elif (x == 3):
        update_grid(2,1)
    elif (x == 4):
        update_grid(2,5)
    elif (x == 5):
        update_grid(2,9)
    elif (x == 6):
        update_grid(4,1)
    elif (x == 7):
        update_grid(4,5)
    elif (x == 8):
        update_grid(4,9)
    else:
        print ('This position is occupied.')
        print_grid()


hello()
print_grid_example()
turn()