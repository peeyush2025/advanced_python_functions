# List Comprehension Practice

nums = [1, 2, 3, 4, 5]

squares = [x**2 for x in nums]
evens = [x for x in nums if x % 2 == 0]
uppercase = [w.upper() for w in ["python", "ai", "code"]]

print(squares)
print(evens)
print(uppercase)
