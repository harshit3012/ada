def gcd1(a, b):
    if(a < b):
        (a, b) = (b, a)
    if(a%b == 0):
        return b
    else:
        return gcd1(b, a%b)
n = int(input("n : "))
m = int(input("m : "))
print(str(gcd1(n, m)))
