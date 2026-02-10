#1RUA25BCA0022_Chiranth D
def fact(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    print(f'factorial for {n} is {f}')

n=int(input("ENTER AN NUMBER:"))
fact(n)
    
#ENTER AN NUMBER:5
#factorial for 5 is 120
