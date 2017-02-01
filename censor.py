def censor(word, text):
    word_array = word.split(' ')
    output = []
    for string in word_array:
        if string == text:
            ast = "*" * len(text)
            output.append(ast)
        else:
            output.append(string)
    return ' '.join(output)
