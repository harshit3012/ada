def toh(n, a, b, c):
    if(n==1):
        print("Plate moved from " + a + " >>> " + c)
    elif(n > 0):
        toh((n-1), a, c, b)
        print(str(n) + " plate moved from " + a + " >>> " + c)
        toh((n-1), b, a, c)
n = int(input("Enter the number of plates : "))
if(n > 0):
    toh(n, 'A', 'B', 'C')
else:
    print("Invalid number of plates!")
