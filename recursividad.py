def recursividad(n, callback):
    callback(n)
    if n == 0:
        return 0
    else:
        return recursividad(n-1, callback)

def callback(x):
    print(x)


print(recursividad(100*2, callback))



