print("welcome to the love calculator")
name1 = input("enter your name: ")
name2 = input("enter the name of your lover: ")

count1 = 0
count2 = 0

name_string = (name1 + name2).lower()

for i in name_string:
    if i == ' ':
        pass
    for j in 'true':
        if i == j:
            count1 += 1

    for k in 'love':
        if i == k:
            count2 += 1
score = int('{}'.format(count1)+'{}'.format(count2))

if score > 90 or score < 10:
    print("Your score is {}, you go together like coke and mentos ".format(score))
elif 40 < score < 50:
    print("your score is {}, you are alright together".format(score))
else:
    print("your score is {}".format(score))
