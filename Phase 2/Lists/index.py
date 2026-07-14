# Creating different types of lists
numbers = [10, 20, 30, 40]
fruits = ["Apple", "Banana", "Mango"]
mixed = ["Aayush", 21, 8.5, True]
empty = []
matrix = [[1, 2], [3, 4]]

# Printing lists
print("Numbers:", numbers)
print("Fruits:", fruits)
print("Mixed:", mixed)
print("Empty List:", empty)
print("Nested List:", matrix)

# Accessing elements using index
print("\nFirst Fruit:", fruits[0])
print("Second Fruit:", fruits[1])
print("Third Fruit:", fruits[2])

# Finding length of a list
print("\nTotal Fruits:", len(fruits))

# Lists allow duplicate values
duplicates = [10, 20, 20, 30, 30]
print("\nDuplicates:", duplicates)

# Lists can store different data types
student = ["Aayush", 21, 8.7, True]
print("\nStudent Info:", student)

# Lists are mutable (modifiable)
fruits[1] = "Orange"
print("\nAfter Modification:", fruits)

# AI Engineering Example
chat_history = [
    "Hello",
    "Explain AI",
    "What is RAG?"
]

print("\nChat History:", chat_history)
print("Latest Message:", chat_history[2])