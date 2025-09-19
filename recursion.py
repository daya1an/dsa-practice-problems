def sumofN(n):
    if n == 1:
        return 1
    return n + sumofN(n - 1)
print("sumofN", sumofN(6))

def factofN(n):
    if n == 1:
        return 1
    return n * factofN(n - 1)
print("factofN",factofN(5))

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)
print("fib",fib(5))


def sumOfList(n):
    # print(n)
    if len(n) == 1:
        return n[-1]
    return n[0] + sumOfList(n[1:])

print("sumOfList",sumOfList([1,2,3,4,5]))

def sumofNestedList(n):
    s = 0
    for i in n:
        if type(i) == type([]):
            s = s + sumofNestedList(i)
        else:
            s = s+i
    return s
print("sumofNestedList",sumofNestedList([1,2,[3,4,[5,6, [7], [8]]]]))

def sumofDigits(n):
    if n//10 == 0:
        return n
    return sumofDigits(n//10) + n%10

print("sumofDigits",sumofDigits(100))

def harmonic(n):
    # s = 0
    # for i in range(1,n+1):
    #     s += 1/i
    # return s
    if n == 0:
        return n
    return harmonic(n-1) + 1/n
print("Harmonic",harmonic(2)) #10 = 2.828968253968254

def power(n,m):
    if m == 1:
        return n
    return n * power(n,m-1)

print("power ",power(2,3))