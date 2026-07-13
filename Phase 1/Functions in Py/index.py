# ==================================
# FUNCTIONS - PYTHON CHEAT SHEET
# ==================================

# 1. Simple Function
def greet():
    print("Hello World")

greet()


# 2. Function with Parameters
def greet(name):
    print("Hello", name)

greet("Aayush")


# 3. Multiple Parameters
def add(a, b):
    print(a + b)

add(10, 20)


# 4. Function with Return (Most Important)
def add(a, b):
    return a + b

result = add(10, 20)
print(result)


# 5. Difference: print() vs return
def square(n):
    print(n * n)          # Only displays

square(5)

def square(n):
    return n * n          # Returns the value

x = square(5)
print(x)


# 6. Default Parameter
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Aayush")


# 7. Keyword Arguments
def student(name, age):
    print(name, age)

student(age=21, name="Aayush")


# 8. Local Variable
def demo():
    x = 10                # Exists only inside this function
    print(x)

demo()


# 9. Global Variable
x = 100

def show():
    print(x)

show()
print(x)


# 10. Function Calling Another Function
def square(x):
    return x * x

def cube(x):
    return x * square(x)

print(cube(3))


# 11. Built-in Functions
print(len("Python"))
print(max(10, 20))
print(min(5, 2))
print(sum([1, 2, 3]))
print(type(100))


# 12. User-defined Function
def area(length, width):
    return length * width

print(area(10, 5))