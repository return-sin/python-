from sympy import factor, symbols
x = symbols('x')
polynomial = x**2 - 5*x + 6
factored_form = factor(polynomial)
print(factored_form)  # 输出：(x - 2)*(x - 3)