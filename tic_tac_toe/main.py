import numpy as np
def hello():
    print ('Hello, let\'s play Tic Tac Toe!')

#Initializes array grid
arr = np.array([[' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
       ['-','-','-','|','-','-','-','|','-','-','-'],
       [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' '],
       ['-','-','-','|','-','-','-','|','-','-','-'],
       [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']])


#Prints example grid with positions
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

#Updates grid
def update_grid(j,k):
    for row in arr:
        arr[j][k] = 'x'

#Prints grid       
def print_grid():
    for row in arr:
        print(' '.join([str(elem) for elem in row]))

#Checks rows
def check_row():
    for row in arr:
        if row[1] == 'x' and row[5] == 'x' and row[9] == 'x':
            print ('You won!')
            return True
    print ('You lost')

#Checks columns           
def check_column():
    for col in arr.T:
        if col[0] == 'x' and col[2] == 'x' and col[4] == 'x':
            print ('You won!')
            return True
    print ('You lost')

#Checks diagonally
def check_diagonally():
    if (arr[0][1] == 'x' and arr[2][5] == 'x' and arr[4][9] == 'x') or (arr[0][9] == 'x' and arr[2][5] == 'x' and arr[4][1] == 'x'):
        print ('You won!')
        return True
    print ('You lost')

#Takes input from user
def turn():
    print ('Please put your mark by entering position on the grid as shown in example above.')
    while (check_row() == True):
        x = input()
        if (x == 0 and arr[0][1] == ' '):
            update_grid(0,1)
        elif (x == 1 and arr[0][5] == ' '):
            update_grid(0,5)
        elif (x == 2 and arr[0][9] == ' '):
            update_grid(0,9)
        elif (x == 3 and arr[2][1] == ' '):
            update_grid(2,1)
        elif (x == 4 and arr[2][5] == ' '):
            update_grid(2,5)
        elif (x == 5 and arr[2][9] == ' '):
            update_grid(2,9)
        elif (x == 6 and arr[4][1] == ' '):
            update_grid(4,1)
        elif (x == 7 and arr[4][5] == ' '):
            update_grid(4,5)
        elif (x == 8 and arr[4][9] == ' '):
            update_grid(4,9)
        else:
            print ('This position is occupied.')
            print_grid()



hello()
print_grid_example()
turn()
print_grid()