# Square Pattern
# for i in range(5):
#     for j in range(5):
#         print('*', end=' ')
#     print()
# Half-Pyramid
# for i in range(1,6):
#     for j in range(i):
#         print('*', end=' ')
#     print()

# Numerical Pyramid
# for i in range(1,6):
#     for j in range(i):
#         print(j+1, end=' ')
#     print()

# For printing same number on each line 
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# for i in range(1,6):
#     for j in range(i):
#         print(i, end=' ')
#     print()

# Inverse Half-Pyramid
# for i in range(6,0, -1):
#     for j in range(i):
#         print('*', end=' ')
#     print()

# Inverse Numerical-Pyramid
# for i in range(6,0, -1):
#     for j in range(1,i):
#         print(j, end=' ')
#     print()

# Half Diamond
# for i in range(1,6):
#     for j in range(1,i):
#         print(' *', end='')
#     print()
# for k in range(6, 0, -1):
#     for l in range(1,k):
#         print(' *', end='')
#     print()

# # Pyramid
# n = 5
# for i in range(1,6):
#     for k in range(n-i):
#         print(' ', end='')
#     for j in range(0,i):
#         print(' *', end='')
#     print()

# # Diamond
# n = 5
# for i in range(1,6):
#     for k in range(n-i):
#         print(' ', end='')
#     for j in range(0,i):
#         print(' *', end='')
#     print()
# for i in range(4,0, -1):
#     for k in range(n-i):
#         print(' ', end='')
#     for j in range(0,i):
#         print(' *', end='')
#     print()