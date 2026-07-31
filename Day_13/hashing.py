# # # Hashing

# # arr=[]
# # size_of_arr = 5
# # for i in range(size_of_arr):
# #     value = int(input(f'Enter {i} element of the array: '))
# #     arr.append(value)
# # print(arr)

# # for i in range(len(arr)):
# #     print(hash(arr[i]))

# # def count_occurrences(arr, query):
# #     count = 0
# #     for num in arr:
# #         if num == query:
# #             count += 1
# #     return count

# # arr = [1, 2, 1, 3, 2]
# # queries = [1, 3, 4, 2, 10]

# # for q in queries:
# #     print(count_occurrences(arr, q))

# arr = [1, 3, 2, 1, 3]
# max_val = 12   # assume we know values won't exceed this

# hash_arr = [0] * (max_val + 1)
# for num in arr:
#     hash_arr[num] += 1

# queries = [1, 4, 2, 3, 12]
# for q in queries:
#     print(hash_arr[q])






# Taking Input Array
s = []

size_of_arr = int(input('Size of the array: '))
for i in range(size_of_arr):
    char = input(f"Enter {i} character of the array: ")
    s.append(char)
print(s)

# Pre-Fetching
hash_arr = [0]*26

query_arr = ['a', 'e', 'f']
count = 0
for char in s:
    hash_arr[ord(char)-ord('a')] += 1

# Compute
for q in query_arr:
    print(f"The {q} occurs",hash_arr[ord(q)-ord('a')], " times" )