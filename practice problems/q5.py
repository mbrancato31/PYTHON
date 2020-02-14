class q5:
    def __init__(self):
        pass
    def getString(self):
        word = input()
        return word

    def printString(self, word):
        print(word)


q = q5()
word = q.getString()
q.printString(word)

# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
#
#     def getString(self):
#         self.s = raw_input()
#
#     def printString(self):
#         print self.s.upper()
#
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()
