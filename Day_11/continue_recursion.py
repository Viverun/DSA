# Print N to 1 using Recursion

# Problem Description: Given an integer N, write a program to print numbers from N to 1.

# Examples
# Input: N = 4
# Output: 4, 3, 2, 1
# Explanation: All the numbers from 4 to 1 are printed.
# Input: N = 1
# Output: 1 
# Explanation: This is the base case.

N = int(input('Enter an integer: '))
count = N
def inverse_count(count):
    if count == 0:
        return
    print(count, end=' ')
    count = count-1
    inverse_count(count)
inverse_count(count)