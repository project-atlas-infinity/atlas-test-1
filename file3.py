# file3.py - Old except, unicode, long
u = unicode("café", "utf-8")
print "Unicode:", u

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError, e:
        print "Division by zero!"
        return 0
    except Exception, e:
        print "Other error:", e

print "10 / 2 =", divide(10, 2)
print "10 / 0 =", divide(10, 0)

l = long(999999999999999999)
print "Long:", l

# Padding
print "Line 20"
print "Line 21"
print "Line 22"
print "Line 23"
print "Line 24"
print "Line 25"
print "Line 26"
print "Line 27"
print "Line 28"
print "Line 29"
print "Line 30"
print "Line 31"
print "Line 32"
print "Line 33"
print "Line 34"
print "Line 35"
print "Line 36"
print "Line 37"
print "Line 38"
print "Line 39"
print "Line 40"
print "Line 41"
print "Line 42"
print "Line 43"
print "Line 44"
print "Line 45"
print "Line 46"
print "Line 47"
print "Line 48"
print "Line 49"
print "Line 50"