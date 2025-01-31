def myRange(stop, start = 0, step = 1):
    while start < stop:
        print(f'Generator Start Value:{start}')
        yield start
        start += step

for i in myRange(10):
    print(f'For Loop Value:{i}')