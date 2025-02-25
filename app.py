def add (a,b):
    return a+b

def remainder (a,b):
    return a%b 

def sum_of_n (n):
    sum = 0
    for i in range(n+1):
        sum +=i
    return sum

def mod(a):
    if a>=0:
        return a
    else:
        return -a

print(mod(add(-7,3)))

print(remainder(1973,7))

print(sum_of_n(100))