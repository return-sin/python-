def square(num):
    num = num + 100
    num = num * num
    num = num + 168
    num = num * num
    return num

num = int(input())
print(square(num))