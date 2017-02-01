def remove_duplicates(num_list):
    unique = {}
    for num in num_list:
        unique[num] = num
    return unique.keys()
