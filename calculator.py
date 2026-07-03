print("Simple Calculator")
a=float(input("Enter a:"))
op=input("Enter operator:")
b=float(input("Enter b:"))
if op=="+":
  print("Answer=",a+b)
elif op=="-":
  print("Answer=",a-b)
elif op=="*":
  print("Answer=",a*b)
elif op=="/":
  if b != 0:
    print("Answer=",a/b)
  else:
    print("Division by 0 not possible")
else:
  print("Invalid Operator")
  
