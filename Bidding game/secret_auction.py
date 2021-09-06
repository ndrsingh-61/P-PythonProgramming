from bid_art import logo
from find_hightest_bidder import *
print(logo)
print("Welcome to the secret auction")


dict_bidding = {}       # empty dictionary is outside the while loop so that loop does not start with an empty list
end_of_bidding = False
while not end_of_bidding:
    bidder_name = input("what is your name: ")
    bid_amount = int(input("enter the amount of bid: "))

    dict_bidding[bidder_name] = bid_amount
    ask_them = input("Are there other users who want to bid: say 'yes' or 'no'")
    if ask_them == 'yes':
        print('\n' * 100)
        end_of_bidding = False

    else:
        print(dict_bidding)
        final_func(dict_bidding)

        end_of_bidding = True


