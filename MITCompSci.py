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


# LECTURE SIX - 6 & 7

# -> Binary search

# Regression testing (func doesn't regress)
# But continues working well

# #of iterations -> speed of convergence

# Non-scalar (Tuple & Strings)
# -> Immutable.

# -> Mutable ->
# List
# L1 = [1,2,3]
# L2 = L1
# print(L2)
# L1[0] = 2
# print(L2)
# print(L1)

# Contra Immutable ->
# a = 1
# b = a
# a = 2
# print(b)
#expects 1

# Mutable cont ->
# Dictionaries
# & unordered
# Generalized indexing
# Key-val pairs dict

# yeah = {'soccer': 'football', 'never': 'jamais'}

# print(yeah['soccer'])
# print(sorted(yeah.keys()))



# LECTURE EIGHT - 8
# Complexity; log, linear, quadratic, exponential algorithms


# Into the weeds of complexity
# What kind of efficiency your code has
# Relate code-choice to efficiency
# Canonical algorithms for classes of complexity ->
# Map new problems into old domains ->

# Rate of growth as size of problem grows
# Asymptotic Notation
# BigO - Upper limit to growth of function as input gets large ->
# f(x)EO(n2)

# Exponents algorithms ->

# This Grows linear ->
def exp1(a,b):
  ans = 1
  while (b>0):
    ans *= a
    b -= 1
  return ans

# print(exp1(2,3))

# Same as 1, but Recursive
# About the same steps, linear
# see @12 for equation

def exp2(a,b):
  if b == 1:
    return a
  else: return a*exp2(a,b-1)

# print(exp2(2,3))

def exp3(a,b):
  if b == 1:
    return a
  # Even case
  if (b%2)*2 == b:
    return exp3(a*a, b/2)
  # Odd case
  else: return a*exp3(a,b-1)

# print(exp3(2,3))
# But rate of growth! ->
# 0(logB)
# Reduce in half


# def g(n,m):
#   x = 0
#   for i in range(n):
#     for j in range(m):
#       x += 1
#   return x
# print(g(2,3))
# O(n2) -> quadratic


# Temple of Hannoi ->
# Discs from one post to another
# exponential ->

# bubble sort -> quadratic
# a linear thing a linear # of times





# LECTURE TEN - 10

# Divide & Conquer algorithm
# Split into several problems of same type
# Solve independent, combine solutions

# ul to sorted -> mergeSort

# EG Algorithm (See Grokking)

# Complexity -> nlogn?
# n -> n2 -> n4 -> base (then merge)
# O(n) operations of each level
# logn - nlogn

# Hash table ->
# Trade space for time ?
# Hard to create good hash-function (go to good library)

# last few lectures ->
# How to learn and identify diff/classes algorithms
# "That looks like a logarithmic algorithm bcs it has..."
# brute force, guess/check, success of apprx, divide & conquer
# What kind of algorithm would be most successful in this case?
#
# Linguistic thing of py -> Exceptions
# See errors (eg asking for "foo" w/o defining)
# Handled Exceptions ->
#     Try: - except: block
# Why? Some things may happen I would like to anticipate
#     Filename (but if not present, do this...)
#     Polymorphic
#
# Whats diff tween exception & assert?
#     Goal of assert = func will give result if... else
#     exception = Do whatever & ima handle it myself... else
#
# Why Exceptions?
#     Best at time of input than 17 calls later



# LECTURE ELEVEN - 11

# Validation -> Process to uncover problems and increase confidence
#     Testing and Reasoning
# Debugging -> Process of ascertaining why program is failing
#
# Defensive programming abet validation & debugging
#
# 2 clases of testing
#     Unit testing (validate each piece indep)
#         Functions
#     Integration testing (all together, does it work?)
#         Big mistake to do right away, usually doesn't work
#         overall
#
# What's so hard about testing?
#     Test suite
#         small enough
#         large enough to boost confidence
#
# 2 best dedugging tools ->
#     print statement
#     reading
#
# [There's no substitute!]
# Be systematic
# Reduce search space
#     localize source of problem
#
# Study program text
#     How could it produce this result?
#     Is it part of a family (systematic throughout?)?
#     How do I fix it?
#
# Scientific method
#     Study available data
#         [all] test results
#         Program text
#     Form hypothesis consistent w/all data
#     Design & implement repeatable experiment
#     [must be able to refute hypothesis]
#         useful intermediate results is nice
#         expected result ->
#
# Use binary search (half it!)
#


# Lecture 12 ->
#
# Bug is prolly not where you think
# Simple things 2 look 4:
#     reversed order of arguments
#         function takes two floats passed in wrong order, eg
#     Spelling
#         You see what you expect 2 see when reading
#     Initialization
#         When var are initialized (inside outside loop, eg)
#     Obj vs. value equality
#     Aliasing
#         Deep vs. shallow copy
#     Side-effects
#     Keep record of what you've tried
#         "Did you do this..." "Idk" Wasting time
#     Reconsider assumptions
#     Debug code, not comments
#         Sometimes comments faulty
#     Get help
#         Swallow pride
#         Explain what progy doing
#             Act has helped identify process
#     Walk away
#         Latency for efficiency?
#
# When found
#     Haste makes waste
#         Think about fixing all symptoms
#         What are ramifications of change?
#             Will it break other things?
#         Does it allow you to tidy other things?
#             Code shouldn't always grow
#         Make sure you can revert
#             Debug to worse than started
#             Save old versions
#
# Algorithms -> Problems (finding solutions)
# Optimization Problems
#     2 parts
#         A function to maximize(min)
#         A set of contraints
#     EG Shortest path problem
#         Time distance, no highways, etc. A2B
#     EG Travelling Salesman
#     EG Bin packing
#         Which order how (tetris)
#     EG Sequence alignment in biology
#         DNA
#     EG Backpack
#         More things than able to take 4 hike
#
# Problem Reduction
#     Is it an instance of another solved problem?
#         Rather than invent my own answer
#


LECTURE 13


Fast fibonacci solutions

Optimal substructure
    Global optimals solution can be constructed
    from optimal solutions to sub-problems

EG
collection objects - a (with total weight)
if size a = n, then 2^n is possible subsets

Decision tree ->
    (depth first, left first)
    don't take 
