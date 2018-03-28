# print(int(9/5), 9%5)

# x = 3
# x = x*x
# print (x)
# n = int(input('enter #: '))
# print(n)
# print n/n

# Can't use
# print (value or command?)
# 28 keywords can't use

# Branching pattern
# can change order of instructions
# based on a test (usually var value)
# x = int(input('x='))
# if (int(x/2))*2 == x:
#   print ('Even')
# else: print ('odd')

# = (assignment)
# == (comparison)

# if <some test>:
#   branch of instructions
# else <some test>:
#   branch of instructions



# x = 15
# y = 5
# z = 11

# print(x,y,z)
# if x < y:
#   if x < z: print('x is least')
#   else: print('z is least')
# else: print('y is least')
# Branch BUG bcs y could b changed to 13 and still considered least

# if x<y and x<z: print('x least')
# elif y<z: print('y least')
# else: print('z least')


# Find sqrt of a perfect square
# x = 16
# ans = 0
# while ans*ans < x:
#   ans = ans + 1
# print(ans)
# better ->

# x = 1515361
# ans = 0
# if x >= 0:
#   while ans*ans < x:
#     ans = ans + 1
#   if ans*ans !=x:
#     print(x, 'is not perf square')
#   else: print(ans)
# else: print(x, 'is neg #')
#Better bcs exhaustive enumeration
#Goes through all reasonable values

#Find all the divisors of an integer
# x = 20
# y = 1
# while y < 20:
#   if x/y == int(x/y):
#     print(y)
#   y = y + 1
# This could b any arbitrary collection


#Another ->
# x = 20
# for i in range(1,x):
#   if x%i == 0:
#     print('divisor', i)

# test = (1,2,3,4,5)
# # Slicing ->
# print(test[1:3])
# # Unto ->
# print(test[:3])
# # From ->
# print(test[3:])
# # All
# print(test[:])

# x = 100
# divisors = ()
# for i in range(1, x):
#   if x%i == 0:
#     divisors = divisors + (i,)
# print(divisors)

# Recursion ->
# def isPalindrome(s):
#   if len(s) <= 1: return True
#   else: return s[0] == s[-1] and isPalindrome(s[1:-1])

# print(isPalindrome('asdffdsa'))

## Palindrome displayed
# def isPalindrome2(s, indent):
#   print(indent, 'isPalindrome2 calld with', s)
#   if len(s) <= 1:
#     print(indent, 'about 2 return True from base case')
#     return True
#   else:
#     ans = s[0] == s[-1] and isPalindrome2(s[1:-1], indent + indent)
#     print(indent, 'About 2 return', ans)
#     return ans

# print(isPalindrome2('racescar', '  '))


# def factorial(x):
#   if x == 0:
#     return 1
#   else:
#     return factorial(x-1) * x

# print(factorial(3))

# def fibonacci(x):
#   if x==0 or x==1: return 1
#   else: return fibonacci(x-1) + fibonacci(x-2)

# print(fibonacci(6))

# py 2 types of numbers ->
# Int - good for counting
  # arbitrary precision #s (big as you want)




# LECTURE FIVE - 5



# a = 2 ** 1000

# x = 0.1
# print(int(x * 10))

# IEEE754 floating point (depreciated) 1.00....01
# Mantissa & Exponent
# Significand ?
# 1 <= Mantissa < 2
#

# https://docs.python.org/2/tutorial/floatingpoint.html

# s = 0.0
# for i in range(10): s += 0.1
# print(s)
# Older versions of py round up to 1 in print

# Worry about == on floats
# eg ->
# ma = 0.1 + 0.2
# # Expect FALSE!
# print("Does .1 + .2 = .3?", 0.1 + 0.2 == .3)
# print(".1 + .2 in python is ", ma)


# import math
# a = math.sqrt(2)
# print(a*a == 2)

# False bcs stored value apprx of sqrt
# Built in == to test floating points NO NO
# SO ->
# Find solution. LOL. Epsilon? -> My import here
# >>> import sys
# >>> sys.float_info.epsilon

# HW -> Read floating point arithmetic &
# Write binary search in py


# LECTURE SIX - 6
