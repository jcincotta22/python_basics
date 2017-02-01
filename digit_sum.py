def digit_sum(n):
    digit_list = []
    digit_list.append(n % 10)
    new_dig = n // 10
    for x in range(n - 1):
        digit_list.append(new_dig % 10)
        new_dig = new_dig // 10
    total = 0
    for n in digit_list:
        total += n
    return total

print digit_sum(1119)
