

input_str = '())('
# def is_balanced(input_str: str):
#     stack = []
#     split_input_str = input_str.split()
#     for element in split_input_str:
#         if element == '(':
#             stack.append(element)
#     return stack
# is_balanced(input_str='(())')
stack = []
split_input_str = list(input_str)
print(split_input_str)

while split_input_str != []:
    found_pair = False
    if split_input_str[0] == ')':
        break
    if split_input_str[0] == '(':
        left_parenthesis = split_input_str.index(split_input_str[0])
        for right_parenthesis_index in range(left_parenthesis+1, len(split_input_str)):
            if split_input_str[right_parenthesis_index] == ')':
                found_pair = True
                right_parenthesis = split_input_str[right_parenthesis_index]
                split_input_str.remove(split_input_str[0])
                split_input_str.remove(right_parenthesis)
                break
    if found_pair == False:
        break
if split_input_str == []:
    print(True)
else:
    print(False)
