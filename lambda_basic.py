squares = [x**2 for x in range(1, 11)]
print filter(lambda x: x >= 30 and x <= 70, squares)
print filter(lambda x: x % 8 == 0, squares)
