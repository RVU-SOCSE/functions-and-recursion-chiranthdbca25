#1RUA25BCA0022_Chiranth D
n = int(input("Enter limit: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Enter limit: 8
#0 1 1 2 3 5 8 13 
