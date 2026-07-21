# Check if a number is Palindrome or Not

# Problem Statement: Given an integer N, return true if it is a palindrome else return false.

# A palindrome is a number that reads the same backward as forward. For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.

# Examples
# Example 1:
# Input:N = 4554
# Output:Palindrome Number
# Explanation: The reverse of 4554 is 4554 and therefore it is palindrome number
                                        
# Example 2:
# Input:N = 7789          
# Output: Not Palindrome
# Explanation: The reverse of number 7789 is 9877 and therefore it is not palindrome

input_num = int(input('Enter a number: '))
num = input_num
rev = 0
while num>0:
    rev_num = num%10
    rev = rev_num + rev*10
    num = num//10

if input_num == rev:
    print(True)
else:
    print(False)