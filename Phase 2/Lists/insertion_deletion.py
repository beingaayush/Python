fruits = ["Apple", "Banana", "Mango"]

# Update an existing element using its index
fruits[1] = "Orange"

# append() -> Adds ONE element at the end
fruits.append("Grapes")

# If a list is passed, it becomes a single element
fruits.append(["Kiwi", "Pineapple"])

print(fruits)

numbers = [10, 20]

# extend() -> Adds multiple elements individually
numbers.extend([30, 40, 50])

# insert(index, value) -> Inserts an element at the given index
numbers.insert(1, 15)

print(numbers)

# ==========================================
# Removing Elements
# ==========================================

nums = [10, 20, 30, 40, 50, 20]

# remove(value) -> Removes the FIRST occurrence of the given value
nums.remove(20)
print(nums)

# pop() -> Removes and returns the last element
last = nums.pop()
print(last)

# pop(index) -> Removes and returns the element at the given index
second = nums.pop(1)
print(second)

print(nums)

# del -> Deletes an element using its index
del nums[0]
print(nums)

# del -> Deletes a range of elements (start included, end excluded)
del nums[1:3]
print(nums)

# clear() -> Removes all elements but keeps the list
nums.clear()
print(nums)

# del -> Deletes the entire list from memory
del nums
# print(nums)   # NameError: 'nums' is not defined