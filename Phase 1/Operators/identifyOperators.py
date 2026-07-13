# Ye check karte hain ki dono variables same object ko refer kar rahe hain ya nahi.
# is
# is not

a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)
print(a == c)

# output:
True
False
True

# Difference:
# == → Values compare karta hai.
# is → Memory object compare karta hai.