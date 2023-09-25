# Assignment

# take the input for the start and stop value for a range.
# Then get the sum of odd and even numbers within that range using function or lambda and display that.

low_range = int(input("Enter a start value for your range: "))
high_range = int(input("Enter a stop value for your range: "))
num = list(range(low_range, high_range+1))
# print(num)
sum_odd = sum(list(filter(lambda x: x % 2 != 0, num)))
sum_even = sum(list(filter(lambda x: x % 2 == 0, num)))
print("Sum of even numbers:",sum_even,"\nSum of odd numbers:",sum_odd)
