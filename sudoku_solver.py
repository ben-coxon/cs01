#!/usr/bin/python

# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(sud):
    size = len(sud[0])
    comp = []
    lst = 0
    a = 1
    
    # Create list of numbers to check for
    for n in sud[0]:
        comp.append(a)
        a += 1
        
    # Create Vertical Numbers List
    vert_list = []
    n = 0
    while n < size:
        clist = []
        for i in sud:
            clist.append(i[n])
        vert_list.append(clist)
        n += 1
        
    # Check horizontal numbers  
    while lst < size:
        for i in comp:
            if not i in sud[lst]:
                print "\nhorizontal Fail!"
                return False
        lst += 1
  
    # Check Vertical Numbers
    lst = 0
    while lst < size:
        for i in comp:
            if not i in vert_list[lst]:
                print "\nvertical Fail!"
                return False
        lst += 1
    
    print "\nThat's Sudoku!"
    return True



### HERE IS THE SOLUTION FROM UDACITY, which is MUCH better!!!

def check_sudoku(p):
	n = len(p) #extract size of grid
	digit = 1 # start with 1
	while digit <= n:  # go through each digit
		i = 0
		while i < n: # go through each row and column
			row_count = 0
			col_count = 0
			j = 0
			while j < n: #for each entry in ith row/column
				if p[i][j] == digit:
					row_count += 1
				if p[j][i] == digit:
					col_count += 1
				j += 1
			if row_count != 1 or col_count != 1:
				return False
			i += 1 # next row/column
			digit += 1 # next digit
		return True # Sudoku was correct!

