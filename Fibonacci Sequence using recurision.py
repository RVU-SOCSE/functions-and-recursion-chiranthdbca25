#1RUA25BCA0022_Chiranth D
def fib(n):
    if n <= 1:
         return n
    else:
        return (fib(n-1) + fib(n-2))

n = int(input("Enter limit: "))
for i in range(n):
    print(fib(i), end=" ")

#Enter limit: 5
#0 1 1 2 3 
