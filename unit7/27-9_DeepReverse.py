# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.


#############################################################

## My Notes:

# This code uses recursion.  

# A list is passed into the function, and we use the range function to iterate 
# in reverse order.  I use the `range(len(list)-1, -1, -1)` syntax, which 
# starts at `len(list)-1` which will be the last index in the list, and continues 
# through the list (note that range continues until one before the second input 
# number, so here we set it to -1, which means range will keep counting to index 0, 
# where we want to stop.  I then set an additional `-1` to indicate we are 
# counting in reverse order i.e. increments of `-1`.

# If an element passing into the function is a list, it will reverse the two 
# items and append to result, whilst calling the `deep_reverse()` function again 
# on each element that is appended. 

# The function uses a base case where the input is not a list.  Any element passing 
# through it should simply return itself (`return list`) if it is not a list.  
# Else it will recurse over the function again, and reverse any innner lists, until 
# they are all single elements.


## My Code:

def is_list(p):
    return isinstance(p, list)

def deep_reverse(p):
    if is_list(p):
        result = []
        for i in range(len(p)-1, -1, -1):
            result.append(deep_reverse(p[i]))

        return result
            
    else:
        return p
    

#############################################################
      

#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
#print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
#print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
#print q
#>>> [1, [2,3], 4, [5,6]]
