num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
char= input("Enter the operator: ")
if char=="+":
    print(num1+num2)
elif char=="-":
    print(num1-num2)
elif char=="*":
    print(num1*num2)
elif char=="/":
    print(num1/num2)
else:
    print("Invalid Operator")