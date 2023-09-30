a=input("enter your name:".lower())
b=input("enter your partner name:".lower())
t=0
r=0
u=0
e=0
l=1
o=1
v=0
e=1
both_name=a+b
t=both_name.count("t")
r=both_name.count("r")
u=both_name.count("u")
e=both_name.count("e")
true=t+r+u+e
l=both_name.count("l")
o=both_name.count("o")
v=both_name.count("v")
e=both_name.count("e")
love=l+o+v+e
print("love calculater\n--------------------------------------------------")
true_love=int(str(true)+str(love))+12
if true_love<=10:
    print(f"your love score {true_love}% you both are just friend")
elif true_love>=11 or true_love<=50:
    print(f"your love score {true_love}% you both are  good lover")
elif true_love >= 51 or true_love <= 90:
    print(f"your love score {true_love}% you both are made for each other")
else:
    print(f"your love score {true_love}% you both are best lover ")