def fact(a):
    if a==0 or a==1:
        return 1
    return a*fact((a-1))

n = int(input("Enter the number to find the factorial of : "))
if n<0:
    print("Invalid input!")
    exit()
print("Factorial of "+str(n)+" is "+str(fact(n)))
