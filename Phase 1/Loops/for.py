# Basic for loop
for i in range(5):
    print(i)              # 0 1 2 3 4


# range(start, stop)
for i in range(1, 6):
    print(i)              # 1 2 3 4 5


# range(start, stop, step)
for i in range(2, 11, 2):
    print(i)              # 2 4 6 8 10


# Reverse loop
for i in range(10, 0, -1):
    print(i)              # 10 to 1


# Loop through a string
name = "Python"

for ch in name:
    print(ch)


# Loop through a list
fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)


# break -> exits the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)


# continue -> skips current iteration
for i in range(6):
    if i == 3:
        continue
    print(i)


# pass -> placeholder (does nothing)
for i in range(3):
    if i == 1:
        pass
    print(i)


# Nested loop
for i in range(3):
    for j in range(2):
        print(i, j)