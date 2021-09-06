import random

name = input("enter the names of the people separated by comas")
name_lst = name.split(',')
who_will_pay = random.randint(0, len(name_lst))
print("{} will pay today".format(name_lst[who_will_pay]))


