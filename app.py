from flask import Flask, request, render_template
import math
from step import steps
from sign import sig
from to_flt_int import flt
app = Flask(__name__)

    
def calculate(a, b, c):
    # Discriminant
    d = ((b**2) - 4*a*c)
    a1 = (-b + d**(1/2)) / (2*a)
    a2 = (-b - d**(1/2)) / (2*a)
    fa, fb, fc = a, b, c

    # Scaling to power of 10
    if abs(a) < 1 and abs(b) < 1 and abs(c) < 1:
        ls = [a, b, c]
        s1 = str(min(ls))
        l1 = len(s1)
        c1 = 0
        for i in range(l1-1, 0, -1):
            if s1[i] == '.':
                break
            else:
                c1 += 1
        scal_fact = 10**c1
        a = round(a * scal_fact)
        b = round(b * scal_fact)
        c = round(c * scal_fact)

    # Scaling to power of 1/10
    if abs(a) > 0 and abs(b) > 0 and abs(c) > 0:
        for i in range(20, 1, -1):
            if a % i == 0 and b % i == 0 and c % i == 0:
                a = a / i
                b = b / i
                c = c / i

    # Recalculate discriminant after scaling
    d = ((b**2) - 4*a*c)
    a1 = (-b + d**(1/2)) / (2*a)
    a2 = (-b - d**(1/2)) / (2*a)
    
    if d == 0:
        e = -b / (2*a)
        return f"{flt(fa)}x²  {sig(flt(fb))}x {sig(flt(fc))} = 0</br> Direct Solution: </br>x = {round(e)}"
    elif a == 0 and b != 0:
        e = -c / b
        return f"{flt(fa)}x²  {sig(flt(fb))}x {sig(flt(fc))} = 0</br> Direct Solution: </br>x = {round(e)}"
    elif d < 0:
        return f"{flt(fa)}x²  {sig(flt(fb))}x {sig(flt(fc))} = 0 </br> Direct Solution: </br> Imaginary roots"
    else:
        return f"{flt(fa)}x²  {sig(flt(fb))}x {sig(flt(fc))}= 0</br> Direct Solution: </br>x = {round(a1)} or x = {round(a2)}"

@app.route('/', methods=['GET', 'POST'])
def solve_quadratic():
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])
#            result = calculate(a, b, c)+steps(a,b,c)
            result=steps(a,b,c)
        except ValueError:
            result = "Invalid input. Please enter numerical values for a, b, and c."
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)


if __name__ == '__main__':
    app.run(debug=True)