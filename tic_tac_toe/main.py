import numpy as np
import random 
import time

#List to hold user anr and computer position
input_list = []
player_list = []


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
    arr1[0][1] = 1
    arr1[0][5] = 2
    arr1[0][9] = 3
    arr1[2][1] = 4
    arr1[2][5] = 5
    arr1[2][9] = 6
    arr1[4][1] = 7
    arr1[4][5] = 8
    arr1[4][9] = 9
    print_grid(arr1)

#Updates grid, takes coordinates and input type as parameters
def update_grid(j,k,type):
    if(type == 'player'):
        arr[j][k] = 'x'
    else:
        arr[j][k] = '0'
    print_grid(arr)

#Prints grid       
def print_grid(grid):
    for row in grid:
        print(' '.join([str(elem) for elem in row]))

#Checks rows
def check_row():
    for row in arr:
        if (row[1] == 'x')*(row[5] == 'x')*(row[9] == 'x'):
            print ('You won!')
            exit()
            return True
        elif (row[1] == '0')*(row[5] == '0')*(row[9] == '0'):
            print ('You lost!')
            exit()
            return True

#Checks columns           
def check_column():
    for col in arr.T:
        if (col[0] == 'x')*(col[2] == 'x')*(col[4] == 'x'):
            print ('You won!')
            exit()
            return True
        elif (col[0] == '0')*(col[2] == '0')*(col[4] == '0'):
            print ('You lost!')
            exit()
            return True

#Checks diagonally
def check_diagonally():
    if (arr[0][1] == 'x')*(arr[2][5] == 'x')*(arr[4][9] == 'x')+(arr[0][9] == 'x')*(arr[2][5] == 'x')*(arr[4][1] == 'x'):
        print ('You won!')
        exit()
        return True
    elif (arr[0][1] == '0')*(arr[2][5] == '0')*(arr[4][9] == '0')+(arr[0][9] == '0')*(arr[2][5] == '0')*(arr[4][1] == '0'):
        print ('You lost!')
        exit()
        return True

#Checks draw
def check_draw():
    if(len(input_list) == 9)*((check_row() != True)+(check_diagonally() != True)+(check_column() != True)):
        print('Noone won. Game over!')
        exit()
        return True

#Check corner
def check_corner():
    if (arr[0][1] == 'x'):
        return 1
    elif(arr[0][9] == 'x'):
        return 3
    elif(arr[4][1] == 'x'):
        return 7
    elif(arr[4][9] == 'x'):
        return 9  
    
#Check edge
def check_edge():
    if (arr[0][5] == 'x'):
        return 2
    elif(arr[2][1] == 'x'):
        return 4
    elif(arr[2][9] == 'x'):
        return 6
    elif(arr[4][5] == 'x'):
        return 8  
    
#check availability
def check_avail(x):
    if (x != 'x')*(x != '0'):
        if (x == 1 and arr[0][1] == ' '):
            return True
        elif (x == 2 and arr[0][5] == ' '):
            return True
        elif (x == 3 and arr[0][9] == ' '):
            return True
        elif (x == 4 and arr[2][1] == ' '):
            return True
        elif (x == 5 and arr[2][5] == ' '):
            return True
        elif (x == 6 and arr[2][9] == ' '):
            return True
        elif (x == 7 and arr[4][1] == ' '):
            return True
        elif (x == 8 and arr[4][5] == ' '):
            return True
        elif (x == 9 and arr[4][9] == ' '):
            return True
    else:
        print('Position is taken. Please enter different')

def pos_next():
    print(input_list)
    print(player_list)

#Validates user position for duplicates
def user_input():
    while True:
        user = input('\nPlease enter your position: ')
        # while True:
        #     if (user == ' '):
        #         print('Position cannot be blank!')
        #     elif (str(user).isdigit() == False):
        #         print('Position can only be integer!')
        #     elif (user > 9)+(user < 0):
        #         print('Podition can only be integer 0-9!')
        if user not in input_list:
            position(user,'player')
            input_list.append(user)
            player_list.append(user)
            check_corner()
            break
        elif(check_draw()): 
            break 
        else:
            print('This position has already been used.')
    return user


#Validates random position for duplicates
def computer_input():
    while True:
        time.sleep(0.5)
        if check_corner() == True and check_avail('5') == True:
            print(check_corner()) 
            pos_next()
            computer = 5
            #break
        elif(check_edge()):
            list = ['1','3','7','9']
            computer = random.choice(list)
        else:
            computer = random.randint(1,9)
        if computer not in input_list:
            print('\nComputer position is: ' + str(computer))
            position(computer,'comp')
            input_list.append(computer)
            break
        elif(check_draw()): 
            break 
    return computer

#Takes turns between user and computer
def turn():
    print ('\nPlease choose your position on the grid as shown in example above.')
    while True:
        if (check_row() == True)+(check_diagonally() == True)+(check_column() == True):
            break
        elif(check_draw()): 
            break 
        user_input()
        computer_input()

#Finds position coordinates on grid
def position(x,type):
    if (x != 'x')*(x != '0'):
        if (x == 1 and arr[0][1] == ' '):
            update_grid(0,1,type)
        elif (x == 2 and arr[0][5] == ' '):
            update_grid(0,5,type)
        elif (x == 3 and arr[0][9] == ' '):
            update_grid(0,9,type)
        elif (x == 4 and arr[2][1] == ' '):
            update_grid(2,1,type)
        elif (x == 5 and arr[2][5] == ' '):
            update_grid(2,5,type)
        elif (x == 6 and arr[2][9] == ' '):
            update_grid(2,9,type)
        elif (x == 7 and arr[4][1] == ' '):
            update_grid(4,1,type)
        elif (x == 8 and arr[4][5] == ' '):
            update_grid(4,5,type)
        elif (x == 9 and arr[4][9] == ' '):
            update_grid(4,9,type)
    else:
        print('Position is taken. Please enter different')



print ('Hello, let\'s play Tic Tac Toe!')
print_grid_example()
turn()

