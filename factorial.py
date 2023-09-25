def fact(n):
    factorial = 1
    if n == 0:
        return 1
    if n >= 1:
        for i in range(1, n + 1):
            factorial = factorial * i
        return factorial


f = int(input("Enter a number: "))

print("Factorial of the given number is: ", fact(f))
