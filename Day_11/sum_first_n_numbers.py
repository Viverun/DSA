# Sum of first N Natural Numbers

# Problem Statement: Given a number ‘N’, find out the sum of the first N natural numbers .

# Examples
# Input: N=5
# Output: 15
# Explanation: 1+2+3+4+5=15

# Input: N=6
# Output: 21
# Explanation: 1+2+3+4+5+6=15

# Using Recursion

N = int(input('Enter the integer: '))
a,b = 0,1
def sum_till_n(a,b):
    if b == N + 1:
        return a
    a = b+a
    b +=1
    # print(a)
    # print(b)
    return sum_till_n(a,b)
result = sum_till_n(a,b)
print(result)
