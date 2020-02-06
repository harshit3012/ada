def hcf(m, n):
    if(n==0):
        return m
    else:
        return hcf(n, m%n)
n = int(input("n : "))
m = int(input("m : "))
print(str(hcf(n, m)))
