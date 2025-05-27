vec = [[1,2,3], [4,5,6], [7,8,9]]

a1 = []
for tab in vec:
    for x in tab:
        a1.append(x)

print(a1)

a2 = [item for tab in vec for item in tab]
print(a2)