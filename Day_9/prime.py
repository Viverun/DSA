# Check if a number is prime or not
# Problem Statement: Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2..

# Examples

# Example 1:
# Input:N = 2
               
# Output:True
                
# Explanation: 2 is a prime number because it has two divisors: 1 and 2 (the number itself).
                                        
# Example 2:
# Input:N =10                
                
# Output: False
                
# Explanation: 10 is not prime, it is a composite number because it has 4 divisors: 1, 2, 5 and 10.                          


int_input = abs(int(input('Enter a number: ')))
divisor_list = []

for i in range(1, int_input+1):
    if int_input%i == 0:
        divisor_list.append(i)
print(f'Output: {divisor_list}')

if len(divisor_list) == 2:
    print('The given number is prime')
else:
    print('The given number is not prime')