values = [10, 10, 20, 20, 20, 30, 10, 10, 40]
result = []
for value in values:
    if not result or value != result[-1]:
        result.append(value)
print("Original List:")
print(values)
print("Result:")
print(result)