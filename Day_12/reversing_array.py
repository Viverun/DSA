# Reverse a given Array

# Problem Statement: You are given an array. The task is to reverse the array and print it.

# Examples
# Input: N = 5, arr[] = {5,4,3,2,1}
# Output: {1,2,3,4,5}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

# Input: N=6 arr[] = {10,20,30,40}
# Output: {40,30,20,10}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

arr = [1, 3, 4, 6, 7]
len_arr = len(arr)
range_of_arr = len_arr//2
for i in range(range_of_arr):
    temp = arr[i]
    arr[i] = arr[len_arr-i-1]
    arr[len_arr-i-1] = temp
print(arr)
