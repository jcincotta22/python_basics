import pdb

def is_lucky(ticket):
    length = len(ticket)
    if ticket == '' or length < 6:
        return False
    sum_1 = 0
    sum_2 = 0
    for x in range(3):
        if ticket[x].isdigit():
            sum_1 += int(ticket[x])
        else:
            return False
    for x in range(length - 3, length):
        if ticket[x].isdigit():
            sum_2 += int(ticket[x])
        else:
            return False
    if sum_1 == sum_2:
        return True
    else:
        return False



# print is_lucky('123321')
