#16K1032松田大輝

import cgi
form=cgi.FieldStorage()
import cgitb
cgitb.enable()

v_t=form.getvalue('t',"0")


template ="""
<head>
    <meta charset="shift-jis">
   <title>E-SHOP</title>
</head>
<html>
<body>
   <p>E-Shop</p>
   <strong>
   Total: {t} JPY<br>
   Thank you !<br>
   </strong>

</body>
</html>
"""
result = template.format(t=v_t)
print("Content-type: text/html\n")
print(result)