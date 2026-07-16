# chars = []
# for ch in "striver":
#     chars.append(ch)
# s = "".join(chars)
# print(chars)

# words = ["Jami", "M"]
# print(", ".join(words))

# def upper(text):
#     return text.upper(  )

# original = "jami"
# result = upper(original)
# print(original)
# print(result)

# s = "striver"
# chars = list(s)
# print(chars)
# chars[0] = 'S'
# print(chars)
# s = "".join(chars)
# print(s)

# arr = [1, 2, 3, 4, 5]

# reversed_arr = []
# for i in range(len(arr) - 1, -1, -1):
#     reversed_arr.append(arr[i])

# print("Manual reverse:", reversed_arr)
# print("Slice reverse:", arr[::-1])
# print("Matches slice reverse:", reversed_arr == arr[::-1])

# usr_int = int(input('Enter your number: '))
# if usr_int >0:
#     print('Number is positive')
# elif usr_int < 0:
#     print('Number is negative')
# else:
#     print('Number is 0')
i = 3
j = 1
numbers = []
while(i>0):
    user_Input = int(input(f'Enter {j} number: '))
    numbers.append(user_Input)
    j = j + 1
    i = i-1

print(numbers)