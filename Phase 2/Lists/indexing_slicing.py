# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# ---------- Positive Indexing ----------
print("First Fruit :", fruits[0])      # Apple
print("Third Fruit :", fruits[2])      # Mango

# ---------- Negative Indexing ----------
print("Last Fruit :", fruits[-1])      # Grapes
print("Second Last :", fruits[-2])     # Orange

# Creating another list
numbers = [10, 20, 30, 40, 50, 60]

# ---------- Basic Slicing ----------
print("\nnumbers[1:4] =", numbers[1:4])   # 20,30,40

# From beginning to index 3 | Omitting start
print("numbers[:4] =", numbers[:4])

# From index 2 till end | Omitting end
print("numbers[2:] =", numbers[2:])

# Complete copy - return entire copy of the list
print("numbers[:] =", numbers[:])

# ---------- Step Slicing ----------
print("\nEvery 2nd Element :", numbers[::2])

# Skip first element, then every 2nd
print("numbers[1::2] =", numbers[1::2])

# ---------- Reverse ----------
print("\nReversed List :", numbers[::-1])

# ---------- Last Three Elements ----------
print("Last 3 Elements :", numbers[-3:])

# ---------- Middle Elements ----------
print("Middle Elements :", numbers[2:5])

# ---------- AI Example ----------
tokens = [101, 2054, 2003, 1037, 102]

print("\nFirst 3 Tokens :", tokens[:3])
print("Last Token :", tokens[-1])
print("Reverse Tokens :", tokens[::-1])