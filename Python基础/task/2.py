i = int(input())
r = 0
if i <10:
    r = i*0.1
elif i<20:
    r = 1+(i-10)*0.075
elif i<40:
    r = 1.75+(i-20)*0.05
elif i<60:
    r = 2.75+(i-40)*0.03
elif i<100:
    r = 3.85+(i-60)*0.015
else:
    r = 3.85+(i-100)*0.01
print("%.2f" % r)