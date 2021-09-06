year_num = int(input("enter the year: "))

if year_num % 4 == 0:
    if year_num % 100 == 0:
        if year_num % 400 == 0:
            print('{} is a leap year'.format(year_num))
        else:
            print("{} is not a leap year".format(year_num))
    else:
        print("{} is a leap year".format(year_num))
else:
    print("{} is not a leap year".format(year_num))
