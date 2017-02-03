def reverse(text):
    x = len(text) - 1
    output = []
    while x > -1:
        output.append(text[x])
        x -= 1
    return ''.join(output)

def reverse_array(array):
    l = len(array)
    output = []
    for x in array:
        output.append(array[l - 1])
        l -= 1
    return output
