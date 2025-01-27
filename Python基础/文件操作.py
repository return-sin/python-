with open("test.txt", "r") as f:
    f.write("hello,world")

with open("test.txt", "r") as f:
    content = f.read()
    print(content)
