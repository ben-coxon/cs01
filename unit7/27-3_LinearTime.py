# For the procedures below, check the procedures whose running time scales linearly 
# with the length of the input in the worst case. You may assume the elements in 
# input_list are fairly small numbers.


def proc1(input_list):
    maximum = None
    for element in input_list :
        if not maximum or maximum < element:
            maximum = element
    return maximum

def proc2(input_list):
    sum = 0
    while len(input_list) > 0:
        sum = sum + input_list[0]   # Assume input_list[0] is constant time
        input_list = input_list[1:]  # Assume input_list[1:] is constant time
    return sum

def proc3(input_list):
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list)):
            if input_list[i] == input_list[j] and i != j:
                return False
    return True

########################################################################
# MY ANSWERS

# proc1 and proc2 scale linearly.  proc3 does not.

# proc1 is iterating through the list once to find the maximum value element, so will 
# scale linearly as input list increases in size.

# proc2 is summing the values of each element, and removing them from the list
# as it loops through.  Therefore it will scale linearly as input size increases.

# proc3 iterates each element in the list, and for each iteration, it iterates the 
# list again to check for duplicate values.  This will exponentially increase the running 
# time as the input size increases.  At worst case, this will be 
# len(input_list) * len(input_list) number of iterations. 




########################################################################
# My Tests to time the procedures. (not really needed in this case, as 
# simply reading the code should be clear which processes scale linearly on not)

test1 = [1, 2, 3]
test2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


import time

def time_execution(code):
	start = time.clock()
	result = eval(code)
	run_time = time.clock() - start
	return result, run_time


print time_execution('proc1(test1)')

print time_execution('proc1(test2)')

print time_execution('proc1(test3)')

print time_execution('proc2(test1)')

print time_execution('proc2(test2)')

print time_execution('proc2(test3)')

print time_execution('proc3(test1)')

print time_execution('proc3(test2)')

print time_execution('proc3(test3)')

