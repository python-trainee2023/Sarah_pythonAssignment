# a_version = open("employee.txt", 'r') Read

# print(a_version.read(3))
# print(a_version.readline())
# print(a_version.readlines())

# for a in a_version.readlines():
#     print(a)

# a_version = open("employee.txt", 'a') Append
# a_version = open("employee.txt", 'w') Write (Overrides the file)
# w+ (write + read)
# a+ (append + read)

a_version = open("employee.txt", 'a')
a_version.write("\nDonut")


a_version.close()
