def factorial(x):
    if x == 1:
        return 1
    multiplier = x
    total = []
    product = 1
    while multiplier > 0:
        total.append(multiplier)
        multiplier -= 1
    for i in total:
        product *= i
    return product

print factorial(12)
