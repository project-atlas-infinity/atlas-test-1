# algorithms.py - tiny algorithms demo (Python 2)

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

if __name__ == '__main__':
    print "Fibonacci 10:", fibonacci(10)
    print "Primes up to 20:", [x for x in range(2,21) if is_prime(x)]
