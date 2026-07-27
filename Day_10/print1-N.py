# Problem Description: Given an integer N, write a program to print numbers from 1 to N.

# Examples
# Input: N = 4
# Output: 1, 2, 3, 4
# Explanation: All the numbers from 1 to 4 are printed.
# Input: N = 1
# Output: 1 
# Explanation: This is the base case.

N = int(input('Enter an integer: '))
counter = 1
def count(counter):
    if counter == N+1:
        return
    if counter == N:
        print(counter, end='')
    else:
        print(counter , end=', ')
    counter += 1
    count(counter)
count(counter)
