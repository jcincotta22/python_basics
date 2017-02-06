def char_count(word):
    word = word.lower()
    output = {}
    for char in word:
        if char in output.keys():
            output[char] += 1
        else:
            output[char] = 1
    for key in output:
        print key + ':', output[key]

char_count('jeffrey cincotta')
