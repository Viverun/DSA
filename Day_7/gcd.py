# # Find GCD of two numbers
# # Problem Statement: Given two integers N1 and N2, find their greatest common divisor.

# # Examples
# # Example 1:
# # Input: N1 = 9, N2 = 12

# # Output: 3
# # Explanation:
# # Factors of 9: 1, 3, 9
# # Factors of 12: 1, 2, 3, 4, 6, 12
# # Common Factors: 1, 3
# # Greatest common factor: 3 (GCD)

# # Example 2:
# # Input: N1 = 20, N2 = 15

# # Output: 5
# # Explanation:
# # Factors of 20: 1, 2, 4, 5, 10, 20
# # Factors of 15: 1, 3, 5, 15
# # Common Factors: 1, 5
# # Greatest common factor: 5 (GCD)

# n1 = 9
# arr1 = []
# n2 = 12
# arr2 = []
# for i in range(1, n1+1):
#     if n1%i == 0:
#         arr1.append(i)
# for j in range(1, n2+1):
#     if n2%j == 0:
#         arr2.append(j)
# print(arr1)
# print(arr2)

# # k = 0; l = 0
# # if len(arr1)<len(arr2):
# #     cmp_arr = len(arr1)
# # else:
# #     cmp_arr = len(arr2)
# # for m in range(1, cmp_arr):
# #     if arr1[m] == arr2[m]:
# #         print(arr1[m])

# set1 = set(arr1)
# set2 = set(arr2)

# intersection_set = set1.intersection(set2)
# print(intersection_set)

# final_list = list(intersection_set)
# print(type(final_list))
# GCD = max(final_list)
# print(f"The GCD of {n1} & {n2} is {GCD}")

# #Now Actual Eucledin Solution
n1 = 12
n2 = 9
orig_n1 = 12
orig_n2 = 9
while n2 !=0:
    n1, n2 = n2, n1%n2
print(f'The GCD of {orig_n1} and {orig_n2} number is {n1}')
