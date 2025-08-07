numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    square = number ** 2 
    squares.append(square)

print(squares)

numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]
print(squares)
