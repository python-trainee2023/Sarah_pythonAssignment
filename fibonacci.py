def fibonacci(n):
    t1 = 1
    t2 = 1
    print(t1)
    print(t2)
    for i in range(2, n):
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        print(t3)


iteration = int(input("Enter the number of fibonancci sequence you want : "))
if iteration <= 2:
    iteration = int(input("Enter number higher than 2: "))
fibonacci(iteration)
