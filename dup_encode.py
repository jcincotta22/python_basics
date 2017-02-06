def duplicate_encode(word):
    word = word.lower()
    single = '('
    double = ')'
    count = {}
    output = ''
    for x in word:
        if x in count.keys():
            count[x] = 2
        else:
            count[x] = 1
    for x in word:
        if count[x] > 1:
            output += double
        else:
            output += single
    return output

print duplicate_encode('Jeffrey')
