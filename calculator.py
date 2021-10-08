num=int(input("enter the num:-"))
num1=int(input("enter the num1:-"))
symbol=input("enter the symbol:-")
if symbol=="+":
    print(num+num1)
elif symbol=="-":
    print(num-num1)
elif symbol=="*":
    print(num*num1)
elif symbol=="%":
    print(num%num1)
elif symbol=="//":
    print(num//num1)
elif symbol=="/":
    print(num/num1)
elif symbol=="**":
    print(num**num1)
else:
    print("nothing is their")