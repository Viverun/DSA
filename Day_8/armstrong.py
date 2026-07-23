# Check if a number is Armstrong Number or not
# Problem Statement:Given an integer N, return true it is an Armstrong number otherwise return false.

# An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
# Examples
# Example 1:
# Input:N = 153
# Output:True
# Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153
                                        
# Example 2:
# Input:N = 371                
# Output: True
# Explanation: 3^3+7^3+1^3 = 27 + 343 + 1 = 371

inputNumber = int(input('Enter the number: '))
copy_inputNumber = inputNumber
listNumber = []
power = 0
while copy_inputNumber > 0:
    copy_inputNumber = copy_inputNumber//10
    power = power + 1
# print(power)
copy_2_inputNumber = inputNumber
while copy_2_inputNumber>0:
    n = copy_2_inputNumber % 10
    listNumber.append(n)
    copy_2_inputNumber = copy_2_inputNumber//10
# print(listNumber)

for i in range(0, power):
    listNumber[i] = (listNumber[i])**power
# print(listNumber)

for i in range(1, power):
    listNumber[i] = listNumber[i] + listNumber[i-1]
    # print(listNumber[i])
# print(listNumber[power-1])
if inputNumber == listNumber[power-1]:
    print('The number is armstrong!')
else:
    print('The number is not armstrong!')