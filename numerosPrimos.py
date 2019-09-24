def isPrime(num):
    if (num % 1 == 0 and num%num == 0):
        for x in range(2, num-1):
            if(num % x == 0):
                return False
        return True
    else:
        return False

for x in range(2, 100000000000000):
    if x%2 != 0 and x % 3 != 0 and x %5 !=0 and x % 7 and x% 9 and x% 11 and x%13:
        if isPrime(x):
            print("\n{}".format(x))

    