print("welcome to pizza corner")
size = input("choose the size of the pizza? small(S), medium(M) or large(L) : ")
add_pepperoni = input("do you want pepperoni? Y or N")
add_cheese = input("do you want extra cheese? Y or N")

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25


if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
# else:
#     bill += 0


if add_cheese == 'Y':
    bill += 1
# else:
#     bill += 0

print("your final bill is : ${}".format(bill))
