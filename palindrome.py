def isPalindrome(s):
    return s == s[::-1]

s = input("Enter a string to check if it's palindrome: ")
print("You Entered:", s)
ans = isPalindrome(s)

if ans:
    print("Yes! Entered string is a palindrome")
else:
    print("No! Entered string is not a palindrome")