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

# import unittest
# # from Experiment import Greeter
#
# class MyTestCase(unittest.TestCase):
#     def test_censor(self):
#         # this test will fail until you change the Greeter to return this expected message
#         self.assertEqual(censor('Hello jeff', 'jeff'), 'Hello ****')
#
# if __name__ == '__main__':
#     unittest.main()
#
# Test.expect(censor('Hello jeff', 'jeff')== 'Hello ****');
