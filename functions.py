# def python_test(n):
#     print("Test Function!! By",n)
#
# python_test("Sarah")

def square(n):
    return n ** 2


def cube(n):
    return n **3


choice = input("Do you want to square(s) or cube(c) a number?")
if choice == "s":
    number = int(input("Enter a number you want the square of: "))
    print(square(number))
else:
    number = int(input("Enter a number you want the cube of: "))
    print(cube(number))
