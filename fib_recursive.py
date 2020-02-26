def fib(a):
    if a<0:
        print("Wrong value!")
        return
    if a==0 or a==1:
        return a
    return fib((a-1))+fib((a-2))

n = int(input("Enter n : "))
print(str(n) + "th Fibonacci number is " + str(fib(n)))
