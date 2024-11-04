def arith_op(a, b, op):
    if(op=='add'):
        result= a+b
    elif(op=='sub'):
        result= a-b
    elif(op=='mul'):
        result= a*b
    return result

inp=''    
while(inp!='4'):
    print("Please choose one of the below options:\n1.Addition\n2.Substraction\n3.Multiplication\n4.Exit")
    inp=input()
    if(inp=="1"):
        print("Enter first number:")
        num1=int(input())
        print("Enter second number:")
        num2=int(input())
        print("Sum is " ,arith_op(num1,num2,'add'))
    elif(inp=="2"):
        print("Enter first number:")
        num1=int(input())
        print("Enter second number:")
        num2=int(input())
        print("Difference is ",arith_op(num1,num2,'sub'))
    elif(inp=="3"):
        print("Enter first number:")
        num1=int(input())
        print("Enter second number:")
        num2=int(input())
        print("Multiplied result is ",arith_op(num1,num2,'mul'))
        
    

