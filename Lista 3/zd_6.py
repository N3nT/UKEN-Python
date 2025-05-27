tekst = "Could not find [platform]"
tekstB = ")independent libraries <prefix>"

def Nawiasy(tekst):
    dict = {"(":")", "[":"]", "{":"}", "<":">"}
    list = []
    for char in tekst:
        if char.isalpha():
            continue
        else:
            if char in dict.keys():
                list.append(char)
            elif char in dict.values():
                if list:
                    list.pop()
                else:
                    return False

    if len(list) == 0:
        return True
    else:
        return False

print(Nawiasy(tekst))
print(Nawiasy(tekstB))