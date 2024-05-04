
a = input("enter your first number:")
op = input("enter your operator:")
b = input("enter your second number:")
if(op== '+'):
  print("the sum of", a, "and", b, "is", int(a) + int(b))
elif(op== '-'):
  print("the subtraction of", a, "and", b, "is", int(a) - int(b))
elif(op== '*'):
  print("the multiplication of", a, "and", b, "is", int(a) * int(b))
elif(op== '/'):
  print("the division of", a, "and", b, "is", int(a) / int(b))
else:
  print("invalid operator")