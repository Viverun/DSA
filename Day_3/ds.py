# #Match -Case statement

# #Traditional method
# # input_number = int(input('Enter from the number 1-7: '))
# # days = {
# #     1:'Monday',
# #     2:'Tuesday',
# #     3:'Wednesday',
# #     4:'Thursday',
# #     5:'Friday',
# #     6:'Saturday',
# #     7:'Sunday'
# # }
# # # .get(key, Default)
# # print(days.get(input_number, "Please choose from 1-7"))

# input_number = int(input('Enter from the number 1-7: '))
# match input_number:
#     case 1: 
#         print('Monday')
#     case 2: 
#         print('Tueday')
#     case 3: 
#         print('Wednesday')
#     case 4: 
#         print('Thursday')
#     case 5: 
#         print('Friday')
#     case 6|7: 
#         print('Weekend')

    
#     case _:
# #         print('Enter the mentioned number!')
    
# #Nested Loop
# for i in range(3):
#     for j in range(3):
#         print(f'i = {i}, j = {j}')


# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
#     print(f'Index={index}: fruit={fruit}')

#Append items in a list using a for loop

# items = []
# for item in range(5):
#     items.append(item)
# print(items)

squares = [i*i for i in range(1, 5)]
print(squares)