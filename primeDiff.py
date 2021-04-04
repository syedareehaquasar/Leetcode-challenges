def firstFactor(n : int, k : int) -> int:
    if n % k == 0:
        return k
    if (k * k) > n:
        return n
    return firstFactor(n, k+1)

def isPrime(n : int) -> bool:
    if n < 2:
        return False
    if n in [2, 3, 5, 7]:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    return firstFactor(n, 11) == n

tc = int(input())
for z in range(tc):
    l, r = map (int, input().split())
    if l > r:
        l, r = r, l
    prime1, prime2 = 0, 0
    for x in range(l, r+1):
        if isPrime(x):
            prime1 = x
            break
    for x in reversed(range(l, r+1)):
        if isPrime(x):
            prime2 = x
            break
    if prime1 == 0 or prime2 == 0:
        print(-1)
    else:
        print(prime2 - prime1)

