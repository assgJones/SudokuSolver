import sys

# this function uses a dictionary to tell us what block a number is in, if we input the index of the tile.
def block (a):
    if a not in range(81):
        return None
    blocks = { 1: [0,1, 2,9,10,11,18,19,20], 2:[3,4,5,12,13,14,21,22,23],3:[6,7,8,15,16,17,24,25,26], 
    4:[27,28,29,36,37,38,45,46,47],5: [30,31,32,39,40,41,48,49,50], 6:[33,34,35,42,43,44,51,52,53],
    7:[54,55,56,63,64,65,72,73,74],8:[57,58,59,66,67,68,75,76,77],9:[60,61,62,69,70,71,78,79,80]}
    for key , value in blocks:
        if a in value: 
            return key
#these next three functions tell us whetehr two indexes are in the same row, column, or block.
def sameRow (a,b):
    return (a/9 == b/9)
    
def sameCol (a,b):
    return (a%9 == b%9)

def sameBlock (a,b):
    return (block (a) == block (b))
#this is a helper to save typing all three of the above.
def sameHelper(a,b):
    return (sameRow (a,b), sameCol (a,b), sameBlock(a,b))
    
# What to do if we have solved  the puzzle
  
def solved(board):
    #at the moment just print the board to the screen
    lines = [[]]
    for tile in board:
        row = tile.index()/9
        lines[row].append(tile)
    for line in lines:
        print (line)
    
    sys.exit (board)

#Solving the puzzle
def solve (board):
    spot = board.find(0)
    if spot == -1:
        solved(board)
    possibilities = findposs (spot)
    if possibilities == None:
        break
    else:
        for pos in possibilities:
            board[spot] = pos
            solve (board)
            
    
def findposs (target):
    possibilities = '123456789'.split
    for b in range(81):
        if (sameHelper(target,b) and (b in possibilities)):
            possibilities.remove(b)
    return possibilities

if len(sys.argv) == 2 and len(sys.argv[1]) == 81:
    solve (sys.argv[1])
  else:
    print 'Usage: python sudoku.py puzzle'
    print '  where puzzle is an 81 character string representing the puzzle read left-to-right, top-to-bottom, and 0 is a blank'
        
    
