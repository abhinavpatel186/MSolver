from to_flt_int import flt
from sign import sig

def steps(a, b, c):
    print_coefficient=""
    generalizing=""
    res=""
    fa, fb, fc = a, b, c
    if abs(a) < 1 and abs(b) < 1 and abs(c) < 1:
        ls = [abs(a), abs(b), abs(c)]
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
        generalizing=(
            f"<pre><br>Multiplying equation {flt(fa)}x² {sig(flt(fb))}x {sig(flt(fc))} = 0 by {scal_fact} we get ..... <br></pre>"
            f"<pre>{flt(a)}x² {sig(flt(b))}x {sig(flt(c))} = 0</pre>"
        )
        # Scaling to power of 1/10
    if abs(a) > 0 and abs(b) > 0 and abs(c) > 0:
        cn=1
        for i in range(20, 2, -1):
            if a % i == 0 and b % i == 0 and c % i == 0:
                cn=cn*i
                a = a / i
                b = b / i
                c = c / i
        if cn>1:
            generalizing=(
                f"<pre><br>dividing equation {flt(fa)}x² {sig(flt(fb))}x {sig(flt(fc))} = 0 by {cn} we get ....... <br></pre>"
                f"<pre>{flt(a)}x² {sig(flt(b))}x {sig(flt(c))} = 0</pre>"
            )

    d = flt(b**2 - 4*a*c)
    

    def main_steps(a,b,c):


        print_coefficient=(
            f"<pre><br><br>Comparing given equation with standard equation....</pre>"
            f"<pre>a = {flt(a)}<br></pre>"
            f"<pre>b = {(flt(b))}<br></pre>"
            f"<pre>c = {flt(c)}<br></pre>"
        )

        if d>=0:
            e = flt(d**0.5)
            f = flt( -b + e )
            g = flt( -b - e )
            h = flt(2*a)
            i = flt(f / h)
            j = flt(g / h)
            quadratic_formula = (
                f"<pre>       b ± √(b² - 4ac)</br></pre>"
                f"<pre>x = --------------------</br></pre>"
                f"<pre>           2a</pre></br></pre>"
            )
            quadratic_formula1 = (
                f"<pre>      {flt(-b)} ± √({flt(b)}² - 4 x {flt(a)} x {flt(c)})</br></pre>"
                f"<pre>x = ----------------------------------------</br></pre>"
                f"<pre>                2 x ({flt(a)})</pre></br></pre>"
            )
            quadratic_formula2 = (
                f"<pre>      {flt(-b)} ± √{(d)}</br></pre>"
                f"<pre>x = -----------------</br></pre>"
                f"<pre>         h</pre></br></pre>"
            )
            quadratic_formula3 = (
                f"<pre>      {flt(-b)} + {(e)}                                         {flt(-b)} - {(e)}</br></pre>"
                f"<pre>x = -------------             or               x = -------------</br></pre>"
                f"<pre>       {h}                                             {h}</pre></br></pre>"
            )
            quadratic_formula4 = (
                f"<pre>         {(f)}                                           {(g)}</br></pre>"
                f"<pre>x = -------------             or               x = -------------</br></pre>"
                f"<pre>        {flt(h)}                                          {flt(h)}</pre></br></pre>"
            )
            quadratic_formula5 = (
                f"<pre>x = {(i)}                        or               x = {(j)}</pre></br>"
            )
        if d>0:
            res= f"{generalizing}<br>{print_coefficient}<br>{quadratic_formula} </br> {quadratic_formula1} </br> {quadratic_formula2} </br> {quadratic_formula3} </br> {quadratic_formula4} </br> {quadratic_formula5} "
        elif d==0:
            quadratic_formula3 = (
                f"<pre>      {flt(-b)} + {flt(e)} </br></pre>"
                f"<pre>x = -------------  </br></pre>"
                f"<pre>       {h}       </pre></br>"
            )
            quadratic_formula4 = (
                f"<pre>         {flt(f)} </br></pre>"
                f"<pre>x = ------------- </br></pre>"
                f"<pre>        {flt(h)}  </pre></br>"
            )
            quadratic_formula5 = (
                f"<pre>x = {flt(i)} </pre></br>"
            )
            res= f"{generalizing}<br>{print_coefficient}<br>{quadratic_formula} </br> {quadratic_formula1} </br> {quadratic_formula2} </br> {quadratic_formula3} </br> {quadratic_formula4} </br> {quadratic_formula5} "
        else:
            quadratic_formula = (
                f"<pre>       b² - 4ac =  {flt(b)}² - 4 x {flt(a)} x {flt(c)}</br></pre>"
                f"<pre>       b² - 4ac =  {flt(b**2)} - {flt(4*a*c)} </br></pre>"
                f"<pre>       b² - 4ac = {d} </br></pre>"
                f"<pre>       AS </br> b² - 4ac <0 </br></pre>"
                f"<pre>Given equation {flt(fa)}x² {sig(flt(fb))}x {sig(flt(fc))} = 0 has imaginary solutions.</pre>"
            )
            res= f"<pre>{generalizing}<br>{print_coefficient}<br>{quadratic_formula}</pre>"

        return f"<pre><br/></br></br>Step Wise Solution: </br> {res}"
#    fsteps=generalizing+print_coefficient+quadratic_formula+quadratic_formula1+quadratic_formula2+quadratic_formula3+quadratic_formula4+quadratic_formula5'''
#    return f"{generalizing}<br>{print_coefficient}<br>{quadratic_formula} </br> {quadratic_formula1} </br> {quadratic_formula2} </br> {quadratic_formula3} </br> {quadratic_formula4} </br> {quadratic_formula5} "
    eg=main_steps(a,b,c)
    sample=eg.split("<br>")
    return sample
#    return main_steps(a,b,c)
