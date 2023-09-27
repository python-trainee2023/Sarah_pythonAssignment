with open("word.txt", "r") as counting:
    count = 0
    data = counting.read()
    words = data.split()
    for word in words:
        if word[-1] == 'e':
            count += 1
    print(count)
counting.close()