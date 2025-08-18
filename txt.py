with open('file.txt', 'r') as file:
    print(file.read())

with open('file.txt', 'a') as file:
    file.write('\n Hello, world!')