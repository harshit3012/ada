def fact(a):
    if a==0 or a==1:
        return 1
    return a*fact((a-1))

n = input("Enter the number to find the factorial of : ")
print("Factorial of "+str(n)+" is "+str(fact(n)))
