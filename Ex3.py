def fibonaci_generator():
    a = 0
    b = 1
    count = 0
    yield a
    yield b
    while (True):
        if a < b:
            a = a+b
            yield a
        else:
            b = a+b
            yield b


fib_gen = iter(fibonaci_generator())


for _ in range(15):
    print(next(fib_gen))
