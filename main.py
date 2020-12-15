row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

p1 = int(position[0]) - 1
p2 = int(position[1]) - 1
map[p1][p2] = "X"

print(f"{row1}\n{row2}\n{row3}")
