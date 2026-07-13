# Normally har print() ke baad next line aa jaati hai.

print("hello")
print("world")

# output:
# hello
# world

# ------------------------------------------------------

# Agar next line nahi chahiye:

# ex1 :
print("hello", end=" ")
print(world)

# output - hello world

# ex2 :
print("Loading", end="...")
print("done")

# output - Loading...done