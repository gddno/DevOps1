def privet(x):
    if x == 0:
        return
    else:
        print("Hello World")
        privet(x-1)
def sum(x):
    if x == 0:
        return 0
    else:
        return x + sum(x-1)
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)


print(fibonacci(10))