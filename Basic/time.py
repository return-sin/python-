import time
d = {}
for i in range(10000000):
    d[i] = 'value'
big_list = [x for x in range(10000000)]

start = time.time()
if 9999999 in d:
    print('Found in dictionary')
end_time = time.time() - start
print('Time taken: ', end_time)

start = time.time()
if 9999999 in big_list:
    print('Found in list')
end_time = time.time() - start
print('Time taken: ', end_time)