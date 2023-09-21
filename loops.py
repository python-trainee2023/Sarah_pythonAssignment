# numbers=[2,4,5,9,13,15,20]
# evens=[]
# print(numbers)
# for i in numbers:
#     if i%2==0:
#         evens.append(i)
# print(evens)

numbers=[1,1.2,2,2.3,4,5,6]

# integer = [x for x in numbers if isinstance(x, int)]
# integer=[x for x in numbers if type(x)==int]
# print(integer)


numbers=input('Enter numbers and seperate by , : ')
n_list = numbers.split(',')
print("Maximum number in ",n_list, " is ", max(n_list))