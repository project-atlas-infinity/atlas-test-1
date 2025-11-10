# file2.py - Python 2: iteritems, raw_input
data = {'a': 1, 'b': 2, 'c': 3}

def print_dict(d):
    for k, v in d.iteritems():
        print "Key:", k, "Value:", v

def update_dict():
    key = raw_input("Enter key: ")
    val = int(raw_input("Enter value: "))
    data[key] = val
    print "Updated!"

print "Initial dict:"
print_dict(data)

try:
    update_dict()
except Exception, e:
    print "Error:", e

print "Final dict:"
print_dict(data)

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