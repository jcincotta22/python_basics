def remove_duplicates(num_list):
    unique = {}
    for num in num_list:
        unique[num] = num
    return unique.keys()

def display_duplicates(num_list):
    dups = []
    unique = {}
    for num in num_list:
        if num in unique.keys() and num not in dups:
            dups.append(num)
        else:
            unique[num] = num
    return sorted(dups)


nums = [1, 2, 2, 3, 4, 5, 5, 7, 8, 11, 12, 11, 1, 2, 15, 12, 99]

print display_duplicates(nums)
