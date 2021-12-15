import random
print("now you  have entered rock,paper,scissor game.Enjoy your game ")
a=input("enter your choice ")
l=["stone","paper","scissor"]
b=random.choice(l)
print(b)
if a==b:
    print("its a draw as the computer chose",b)
elif a=="stone" and b=="paper":
    print("defeated as the computer chose ",b)
elif a=="stone" and b=="scissor":
    print("won as the computer chose ", b)
elif a=="paper" and b=="scissor":
    print("defeated as the computer chose ", b)
elif a=="paper" and b=="stone":
    print("won as the computer chose ", b)
elif a=="scissor" and b=="stone":
    print("defeated as the computer chose ", b)
elif a=="scissor" and b=="paper":
    print("won as the computer chose ", b)
else:
    print("hi")
