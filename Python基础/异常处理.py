try:
    num = int(input("请输入一个数字："))
    print(10 / num)
except ZeroDivisionError:
    print("不能除以零")
except ValueError:
    print("请输入有效数字")
