def hcf(a, b):
    if(a < b):
        (a, b) = (b, a)
    if(a%b == 0):
        return b
    else:
        return hcf(b, a%b)
n = int(input("n : "))
m = int(input("m : "))
print(str(hcf(n, m)))
