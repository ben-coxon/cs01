#!/usr/bin/python

# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def vert_list(l, pos):
    new_list = []
    length = len(l)
    i = 0
    while i < length:
        if len(l[i]) != length:
            new_list = []
            break
        else:
            new_list.append(l[i][pos])
            i += 1
    return new_list


def symmetric(p):
    n = len(p) #extract size of grid
    i = 0
    count = 0
    while i < n:
        if p[i] == vert_list(p, i):
            count += 1
        i += 1
    if count == n:
        return True
    return False
        
print symmetric([['cricket', 'football', 'tennis'], 
                ['golf']])

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False