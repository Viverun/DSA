
def factorial(num_posts):
    if num_posts == 0 or num_posts ==1:
        return 1
    for i in range(num_posts-1, 0, -1):
        num_posts = num_posts * (i)
    return num_posts
value = factorial(3)
print(value)
