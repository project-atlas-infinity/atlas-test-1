# file5.py - reduce, map, filter, apply
from functools import reduce

nums = range(1, 6)
squared = map(lambda x: x*x, nums)
print("Squared:", list(squared))

evens = filter(lambda x: x % 2 == 0, range(10))
print("Evens:", list(evens))

total = reduce(lambda x, y: x + y, range(1, 11), 0)
print("Sum 1..10:", total)

def func(a, b):
    return a * b

print("apply(func, (3, 4)):", func(*(3, 4)))

# Padding
print("Line 20")
print("Line 21")
print("Line 22")
print("Line 23")
print("Line 24")
print("Line 25")
print("Line 26")
print("Line 27")
print("Line 28")
print("Line 29")
print("Line 30")
print("Line 31")
print("Line 32")
print("Line 33")
print("Line 34")
print("Line 35")
print("Line 36")
print("Line 37")
print("Line 38")
print("Line 39")
print("Line 40")
print("Line 41")
print("Line 42")
print("Line 43")
print("Line 44")
print("Line 45")
print("Line 46")
print("Line 47")
print("Line 48")
print("Line 49")
print("Line 50")
