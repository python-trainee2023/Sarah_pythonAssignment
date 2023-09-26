with open("student01.txt", "r") as f, open("student02.txt", "a") as g:
    for students in f:
        g.write(students.upper())
print("Data copied")
print(f.closed)