


def isPrimeUpdate(num, arr):
    for y in arr:
        if num % y == 0:
            return False      
    for x in range(2, num-1):
            if(num % x == 0):
                return False
    return True


def isPrime(num):      
    for x in range(2, num-1):
            if(num % x == 0):
                return False
    return True
a = []
for x in range(2, 100000):
    if isPrime(x):
        a.append(x)
    # if(isPrime(y-1)):
        # print(y-1)
    
    # print(y)
# if isPrime(x):
#     print("\n{}".format(x))
print(a)
for h in range(2, 100000000000000):
    if isPrimeUpdate(h, a):
        print(h)


 

    