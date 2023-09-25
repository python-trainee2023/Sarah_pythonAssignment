a_version = open("employee.txt", 'r')

# print(a_version.read(3))
# print(a_version.readline())
# print(a_version.readlines())

for a in a_version.readlines():
    print(a)
a_version.close()
