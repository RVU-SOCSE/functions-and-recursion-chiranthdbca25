#1RUA25BCA0022_Chiranth D
def factorial(n):
    if n == 0 or n == 1:
      return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))

#Enter a number: 5
#Factorial: 120



