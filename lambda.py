addition = lambda a, b: a + b
print(addition(2, 3))

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = list(filter(lambda x: x % 2 == 0, num))
print(even)
sq = list(map(lambda x: x ** 2, num))
print(sq)

operations = [lambda x, y: x + y, lambda x, y: x - y]
print(operations[0](1, 2), operations[1](3, 2))
