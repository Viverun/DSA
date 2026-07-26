# # Print all Divisors of a given Number
# # Problem Statement: Given an integer N, return all divisors of N.
# # A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

# # Examples
# # Input: N = 36
# # Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]  
# # Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.
# # Input: N = 12
# # Output: [1, 2, 3, 4, 6, 12]
# # Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.

# int_input = abs(int(input('Enter a number: ')))
# divisor_list = []

# for i in range(1, int_input+1):
#     if int_input%i == 0:
#         divisor_list.append(i)
# print(f'Output: {divisor_list}')

n = abs(int(input("Enter a number: ")))
divisors = []

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        divisors.append(i)

        if i != n // i:      # avoid duplicate for perfect squares
            divisors.append(n // i)

divisors.sort()
print(divisors)