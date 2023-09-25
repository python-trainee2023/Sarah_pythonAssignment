# def fact(n):
#     factorial = 1
#     if n == 0:
#         return 1
#     if n >= 1:
#         for i in range(1, n + 1):
#             factorial = factorial * i
#         return factorial
def recursive_fact(n):
    if n == 0:
        return 1
    else:
        return n * recursive_fact(n - 1)


f = int(input("Enter a number: "))

print("Factorial of the given number is: ", recursive_fact(f))
