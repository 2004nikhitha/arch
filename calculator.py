operator=input("enter an operator(+-*/):")
num1=float(input("enter the 1st number:"))
num2=float(input("enter the 2nd number:"))
if operator=="+":
    result=num1+num2
    print(round(result ))
elif operator=="-":
    result =num1-num2
    print(round(result))
elif operator=="*":
    result=num1*num2
    print(round(result ))
elif operator=="/":
    result=num1/num2
    print(round(result ))
else:
    print("(operator) is not a valid operator")
     
      

