# def docorator(func):
#     def wrap():
#         print('==============')
#         func()
#         print('==============')
#     return wrap

# @docorator
# def printName():
#     print('Mike')
# printName()

# ============================================
# def run_time(num):
#     def wrap(func):
#         for i in range(num):
#             func()
#     return wrap

# @run_time(3)
# def printName():
#     print('Mike')

# ============================================
# def birthday(func):
#     def wrap(name, age):
#         func(name, age+1)
#     return wrap

# @birthday
# def celebrate(name, age):
#     print('Happy birthday', name, 'You are now', age)
# celebrate('Mike', 18)

# ============================================
def login_required(func):
    def wrap(user):
        password = input('Enter your password:')
        if password == user['password']:
            func(user)
        else:
            print('Password is wrong')
    return wrap

@login_required
def restrictedFunc(user):
    print('Access granted:', user['name'])

user = {'name':'Mike', 'password':'1234'}
restrictedFunc(user)

