def commaCode(listValue):
    text=''
    for i in range(len(listValue)):
        if i == len(listValue) - 1:
            text += 'and ' + str(listValue[i])
        else:
            text += str(listValue[i]) + ', '
    return text

spam = ['apples', 'bananas', 'tofu', 'cat']
print(commaCode(spam))