def hello(custom):
    if not isinstance(custom, str):
        raise TypeError('custom is not a string')
    if custom == '':
        raise ValueError('custom is empty')
    print(f'Hello {custom}')


try:
    hello(222)
except ValueError as e:
    print(e)
    print('custom is empty')
except TypeError as e:
    print(e)
    print('custom is not a string')

print('end of program')