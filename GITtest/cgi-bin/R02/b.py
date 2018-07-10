#16K1032松田大輝

import cgitb
cgitb.enable()
import cgi
form=cgi.FieldStorage()

v1 = form.getvalue('Pen', '0')
v2 = form.getvalue('Note', '0')
v3 = form.getvalue('Eraser', '0')
v4 = form.getvalue('Tape', '0')
v5 = form.getvalue("Scissors","0")
v6 = form.getvalue("Stapler","0")
room=form.getvalue("room")

p=[100,200,300,400,500,600]

template ="""
<head>
    <meta charset="UTF-8">
   <title>E-SHOP</title>
   <link rel="stylesheet" type="text/css" href="../../2.css">
</head>
<html><body>

   <div class="flexbox">
   <section class="main">

    <form method="" action="http://localhost:8000/cgi-bin/R02/b.py">

    <img src="../../img/1.jpg"><br>
    Pen<br>
    100 JPY
    <p><input type="text" name="Pen" value="0"> </p>

    <img src="../../img/2.jpg"><br>
    Note<br>
    200 JPY
    <p><input type="text" name="Note" value="0"></p>

    <img src="../../img/3.jpg"><br>
    Eraser<br>
    300 JPY
    <p><input type="text" name="Eraser" value="0"></p>


    </section>
  <section class="main2">


    <img src="../../img/4.jpg"><br>
    Tape<br>
    400 JPY
    <p><input type="text" name="Tape" value="0"></p>

    <img src="../../img/5.jpg"><br>
    Scissors<br>
    500 JPY
    <p><input type="text" name="Scissors" value="0"></p>

    <img src="../../img/6.jpg"><br>
    Stapler<br>
    600 JPY
    <p><input type="text" name="Stapler" value="0"></p>

    <br><br>

    <p><input type="submit" value="カートへ"><input type="reset" value="リセット"></p>
    </form>
  </section>


  <section class="side">
    <h1>CART</h1>

   <strong>
   {Pen}<br>
   {Note}<br>
   {Eraser}<br>
   {Tape}<br>
   {Scissors}<br>
   {Stapler}<br>
   <br><br>

   <h2>TOTAL PRICE</h2>
   {total} JPY


<p><a href = "/cgi-bin/R02/c.py?t={total}">
   CHECK OUT
   </a></p>

    </section>
</div>
   </strong>

</body></html>
"""

t=p[0]*int(v1)+p[1]*int(v2)+p[2]*int(v3)+p[3]*int(v4)+p[4]*int(v5)+p[5]*int(v6)

result = template.format(Pen=("Pen", v1),
                         Note=("Note", v2),
                         Eraser=("Eraser", v3),
                         Tape=("Tape", v4),
                         Scissors=("Scissors", v5),
                         Stapler=("Stapler",v6),
                         total=(t),
                         r=(room))
print("Content-type: text/html\n")
print(result)