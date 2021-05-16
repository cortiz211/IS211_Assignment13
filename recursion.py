
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def gcd(a, b):
    if b == 0:
        return b
    else:
        gcd(b, a % b)

def compareto(s1, s2):

    if s1 < s2:
        return -1
    elif s1 == s2:
        return 0
    else:
        return 1

if __name__ == "__main__":
    for x in range(5):
        print(fibonacci(x))
    print(gcd(20,12))
    print(compareto(5,5))