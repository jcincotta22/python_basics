def anti_vowel(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    output = ''
    for char in text:
        if char not in vowels:
            output += char
    return output
