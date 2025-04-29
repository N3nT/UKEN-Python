n = int(input("Podaj n: "))
# a.
print("A: ")
i = 0
while i < n:
    i += 1
    print(i, end=" ")
print()
for i in range(1, n+1):
    print(i, end=" ")
print()

# b.
print("B: ")
i = n
while i >= 1:
    print(i, end=" ")
    i = i - 1
print()
for i in range(n, 0, -1):
    print(i, end=" ")
print()

# c.
print("C: ")
i = 0
while i < n:
    i += 1
    if i % 2 == 0:
        print(i, end=" ")
print()
for i in range(1, n+1):
    if i % 2 == 0:
        print(i, end=" ")
print()

# d.
print("D: ")
i = 0
while i < n:
    i += 1
    if i % 2 != 0:
        print(i, end=" ")
print()
for i in range(1, n+1):
    if i % 2 != 0:
        print(i, end=" ")
print()

# e.
print("E: ")
i = 1
while i <= n:
    print(i, end=" ")
    i += 3
print()
for i in range(1, n+1, 3):
    print(i, end=" ")
print()

# f.

print("F: ")
