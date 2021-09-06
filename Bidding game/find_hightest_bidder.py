def final_func(dict_bid):
    maxim = 0
    winner = ""
    for key in dict_bid:
        values = dict_bid[key]
        if values > maxim:
            maxim = values
            winner = key

    print("The winner is {} with a bid of ${}".format(winner, maxim))
