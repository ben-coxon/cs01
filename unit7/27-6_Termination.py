
# Termination

# For each of the procedures defined below, check the box if the 
# procedure always terminates for all inputs that are natural 
# numbers (1,2,3...).

## MY ANSWER:

## proc1() and proc3() will always terminate for whole numbers above 0.
## proc1() will eventually reach n == 0 and break.  proc3() will eventually 
## find the value of n equal or below 4 and return.
## However, in the case of proc2(), if the input is 1, it will immediately
## become below 0, and never hit the n == 0 base-case.


def proc1(n):
   while True:
      n = n - 1
      if n == 0:
         break
   return 3


def proc2(n):
   if n == 0:
      return n
   return 1 + proc2(n - 2)

def proc3(n):
   if n <= 3:
      return 1
   return proc3(n - 1) + proc3(n - 2) + proc3(n - 3)



################################################################

################################################################
# TESTS





# The below example fors into an infinte loop, as n immediately
# drops below 0, so does not execute the base-case.  However, 
# the question specifies natural numbers as starting with 1.
print proc1(0)


# The below example does not terminate, as n immediately drops
# below 0, so does not terminate with the base-case.  This will 
# happen with all odd numbers!
# Error is:  RuntimeError: maximum recursion depth exceeded
print proc2(1)


print proc3(10)







