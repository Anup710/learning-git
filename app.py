def add (a,b):
    return a+b

def remainder (a,b):
    return a%b 

def mod(a):
    if a>=0:
        return a
    else:
        return -a

print(mod(add(-7,3)))

print(remainder(1973,7))