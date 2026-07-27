''' Recursion
--- When a function calls itself until a specified condition is met

Q1) Print Name N times using Recursion

Problem Description: Given an integer N, write a program to print your name N times.
Examples
Input: N = 3
Output: Ashish Ashish Ashish 
Explanation: Name is printed 3 times.
Input: N = 1
Output: Ashish 
Explanation: Name is printed once.
'''
name = input('Enter your name: ')
count = int(input('Enter the number of times you want to count your name: '))
initializer = 0
# def count_name(initializer):
#     initializer += 1
#     print(name, end=' ')
#     if initializer<count:
#         count_name(initializer)
# count_name(initializer)

def count_name(initializer):
    if initializer == count:
        return None
    else:
        print(name, end=' ')
        initializer += 1
        count_name(initializer)
count_name(initializer)