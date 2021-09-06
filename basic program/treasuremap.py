row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
maps = [row1, row2, row3]

print("{}\n{}\n{}".format(row1, row2, row3))
position = (input("enter the row and column"))
column = int(position[0])
row = int(position[1])
maps[column-1][row-1] = 'x'
print("{}\n{}\n{}".format(row1, row2, row3))


