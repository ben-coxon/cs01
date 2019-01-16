# Question 2. Triangular Numbers

# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Write a procedure, triangular, that takes as its input a positive 
# integer n and returns the nth triangular number.

    
def triangular(n):
    result = 0
    for i in range(1, n + 1):
        result += i
        print result
    return result


print "Result: " + str(triangular(1))
#>>>1
print ""

print "Result: " + str(triangular(3))
#>>> 6
print ""

print "Result: " + str(triangular(10))
#>>> 55
print ""