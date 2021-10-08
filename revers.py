num=int(input("enter the num="))
sum=0
rev=0
while num>0:
    rev=rev*10+(num%10)
    num=num//10 
a=rev
while a>0:
    r=a%10
    b=r*r
    c=b
    a=a//10
    print(c,end="")
print()