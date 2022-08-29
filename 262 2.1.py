num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print("enter any two numbers")
ch=input("enter any of these char for specific orientation +,-,*,/:")
result=0
if ch=='+':
    result=num1+num2
elif ch=='-':
    result=num1-num2
elif ch=='*':
    result=num1*num2
elif ch=='/':
    result=num1/num2
else:
    print("Input character is not recognized!")
print(num1,ch,num2,":",result)
