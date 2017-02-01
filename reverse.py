def reverse(text):
    x = len(text) - 1
    output = []
    while x > -1:
        output.append(text[x])
        x -= 1
    return ''.join(output)
