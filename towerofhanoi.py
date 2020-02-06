def toh(n, a, b, c):
    if(n==1):
        print("Plate moved from " + a + " >>> " + c)
    elif(n > 0):
        toh((n-1), a, c, b)
        print(str(n) + " plate(s) moved from " + a + " >>> " + c)
        toh((n-1), b, a, c)
n = int(input("Enter the number of plates : "))
toh(n, 'A', 'B', 'C')

