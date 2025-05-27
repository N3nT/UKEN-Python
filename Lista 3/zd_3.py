matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
transponowana = [[],[],[],[]]

i = 0

while i <= len(matrix):
    for tab in matrix:
        if i%4==0:
            transponowana[0].append(tab[i])
        elif i%4==1:
            transponowana[1].append(tab[i])
        elif i%4==2:
            transponowana[2].append(tab[i])
        elif i % 4 == 3:
            transponowana[3].append(tab[i])
    i+=1

print(transponowana)