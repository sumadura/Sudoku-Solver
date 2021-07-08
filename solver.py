board = [
        [0, 0, 0, 0, 5, 7, 1, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 7, 0, 0, 9, 0, 2, 4, 0],
        [0, 0, 0, 0, 0, 9, 8, 5, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 2, 8, 4, 0, 0, 0, 0, 0],
        [0, 3, 6, 0, 1, 0, 0, 8, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 9, 7, 6, 0, 0, 0, 0]
    ]

def print_board(b):                                 #b - board 
    """
    Doc String

    Parameter: list of lists of numbers i.e., board
    -------
    Returns: board with partitions as an actual sudoku board

    """
    
    for i in range(len(b)):
        if i%3 == 0 and i != 0:
            print("---------------------")
        for j in range(len(b[0])):
            if j%3 == 0 and j != 0:
                print("|",end=' ')
                
            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]),end=' ')
                

def pick_empty(b):
    """
    Doc String

    Parameter: list of lists of numbers i.e., board
    -------
    Returns: (row,col) of empty square
             and if there is no such square, returns False

    """
    
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i,j)  
                     
    return None                                  
            

def valid(b, n, p):                                  #n - number; p - position
    """
    Doc String

    Parameter: list of lists of numbers i.e., board
               number that has to be checked
               position of the number
    -------
    Returns: True if the number is valid 
             False if its not valid

    """
    
    for i in range(len(b[0])):
        if b[p[0]][i] == n and i != p[1]:
            return False
        
    for i in range(len(b)):
        if b[i][p[1]] == n and i != p[0]:
            return False
    
    box_i = p[0]//3
    box_j = p[1]//3
    
    for i in range((box_i*3),(box_i*3)+3):
        for j in range((box_j*3),(box_j*3)+3):
            if b[i][j] == n and (i,j) != p:
                return False
            
    return True
            

def solve(b):
    """
    Doc String

    Parameter: list of lists of numbers i.e., board
    -------
    Returns: the right value at empty square positions

    """
    find = pick_empty(b)
    if not find:
        return True
    else:
        row,col = find
        
    for i in range(1,10):
        if valid(b, i, (row,col)):
            b[row][col] = i
            
            if solve(b):
                return True
            
            b[row][col] = 0
            
    return False


print("The board is: ")
print_board(board)

solve(board)

print("")
print("The solution for the board is : ")
print_board(board)