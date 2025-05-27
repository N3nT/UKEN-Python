keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

newDict = {klucz: values for klucz, values in zip(keys, values)}

print(newDict)

newDict['e'] = sum(newDict.values())

print(newDict)

newDictTwo = {klucz: values ** 2 for klucz, values in newDict.items()}
print(newDictTwo)

newDictThree = {klucz: values for klucz, values in newDictTwo.items() if values < 10}
print(newDictThree)


