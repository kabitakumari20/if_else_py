user=input("enter the string:-")
a=len(user)
if a>=3 and "ing" not in user:
    print(user+"ing")
elif a>3 and "ing" in user:
    print(user+"ly")
else:
    print("nothing")