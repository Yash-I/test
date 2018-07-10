#16k1032
#松田大輝

import cgi
form=cgi.FieldStorage()
import cgitb
cgitb.enable()

v_n=form.getvalue('n',"0")
v_from=form.getvalue('from')
v_to=form.getvalue('to')


template ="""
<head>
    <meta charset="shift-jis">
   <title>PRICE</title>
</head>
<html>
<body>
   <p>DETAIL</p>
   <strong>
   Fare from {from1} to {to} : {price} JPY<br>
   {n} adults : {total} JPY
   </strong>
   <form method="GET" action="/cgi-bin/L10/ex1.py">
   <p> apple: <input type="text" name="apple"> </p>
   <p> orange: <input type="text" name="orange"></p>
   <p><input type="submit"></p>
   </form>
</body>
</html>
"""

a=0
b=int(v_n)
stations=["Shinjuku","Nakano","Mitaka"]
if v_from in stations and v_to in stations:

    if v_from==v_to:
        a=0
    else:
        a=154

result = template.format(from1=v_from,to=v_to,price=a,n=b,total=a*b)
print("Content-type: text/html\n")
print(result)