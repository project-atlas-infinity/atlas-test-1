# file1.py - Python 2 demo: print and xrange
print "Starting file1 processing..."

def generate_numbers(n):
    for i in xrange(n):
        print "Number:", i
    return list(xrange(n))

def main():
    print "Generating 10 numbers..."
    nums = generate_numbers(10)
    print "Done. Count:", len(nums)

if __name__ == "__main__":
    main()
    print "file1 complete."

# Padding lines to reach 50
print "Line 15"
print "Line 16"
print "Line 17"
print "Line 18"
print "Line 19"
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