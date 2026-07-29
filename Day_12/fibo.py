# Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

# Examples
# Input: N = 5
# Output: 0 1 1 2 3 5
# Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

# Example 2:
# Input: 6
# Output: 0 1 1 2 3 5 8
# Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)

N = int(input("Enter the number: "))
n = N
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    n = fibo(n-1) + fibo(n-2)
    return n
for i in range(n+1):
    print(fibo(i), end=' ')