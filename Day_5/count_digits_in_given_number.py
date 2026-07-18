# Example 1:
# Input:N = 12345
# Output:5
# Explanation:  The number 12345 has 5 digits.
                        
# Example 2:
# Input:N = 7789              
# Output: 4
# Explanation: The number 7789 has 4 digits.  

# Base Approach(How I did that!)
# number = abs(int(input('Enter a number: ')))
# str_num = str(number)
# count = len(str_num)
# print(f'The number of digits in given number is: {count} ')

# #DSA Approach!
# import math
# count = 0
# number = abs(int(input('Enter a number: ')))
# if number == 0:
#     count = 1
# else :
#     count = int(math.log10(number)) + 1
# print(count)