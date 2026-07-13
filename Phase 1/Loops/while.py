# Basic while loop
i = 1

while i <= 5:
    print(i)
    i += 1                 # Update variable (important)


# Reverse counting
i = 10

while i >= 1:
    print(i)
    i -= 1


# Sum of first 5 numbers
i = 1
total = 0

while i <= 5:
    total += i
    i += 1

print(total)


# break -> exits loop immediately
i = 1

while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1


# continue -> skips current iteration
i = 0

while i < 5:
    i += 1

    if i == 3:
        continue

    print(i)


# pass -> placeholder
i = 1

while i <= 3:
    if i == 2:
        pass

    print(i)
    i += 1


# Infinite loop (Don't run this)
# while True:
#     print("Running forever...")


# Nested while loop
i = 1

while i <= 3:
    j = 1

    while j <= 2:
        print(i, j)
        j += 1

    i += 1