# file7.py - Old-style class, __metaclass__
class OldClass:
    __metaclass__ = type
    def __init__(self):
        self.value = 42
    def get_value(self):
        return self.value
    def __str__(self):
        return "<OldClass %d>" % self.value

obj = OldClass()
print obj
print "Value:", obj.get_value()

inst = OldClass()
print "Same?", inst is obj

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