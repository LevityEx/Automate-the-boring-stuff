list = ['apples', 'bananas', 'tofu', 'cats']
result = "'"
def createString():
    global result
    for index, item in enumerate(list):
        if((index + 1) == len(list)):
            result += 'and ' + item + "'."
        else:
            result += item + ", "
    return result
print(createString())


