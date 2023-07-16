import random
def x_o():
    row_1 = ["■", "■", "■"]
    row_2 = ["■", "■", "■"]
    row_3 = ["■", "■", "■"]
    map = [row_1, row_2, row_3]
    print(f"{row_1}\n{row_2}\n{row_3}")
    while True:
        coordinates = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]
        your_choice = input("Where do you want (rowcolumn)?\n")
        index_1 = coordinates.index(your_choice)
        coordinates.pop(index_1)
        computer = random.choice(coordinates)
        index_2 = coordinates.index(computer)
        coordinates.pop(index_2)
        h = int(your_choice[0])
        v = int(your_choice[1])
        h1 = int(computer[0])
        v1 = int(computer[1])
        map[v - 1][h - 1] = "X"
        map[v1 - 1][h1 - 1] = "O"
        print(f"{row_1}\n{row_2}\n{row_3}")
        if map[0][0] == "X" and map[0][1] == "X" and map[0][2] == "X" or map[0][0] == "O" and map[0][1] == "O" and map[0][2] == "O":
            print(f"Congratulations to {map[0][0]}!")
            break
        elif map[1][0] == "X" and map[1][1] == "X" and map[1][2] == "X" or map[1][0] == "O" and map[1][1] == "O" and map[1][2] == "O":
            print(f"Congratulations to {map[1][0]}!")
            break
        elif map[2][0] == "X" and map[2][1] == "X" and map[2][2] == "X" or map[2][0] == "O" and map[2][1] == "O" and map[2][2] == "O":
            print(f"Congratulations to {map[2][0]}!")
            break
        elif map[0][0] == "X" and map[1][1] == "X" and map[2][2] == "X" or map[0][0] == "O" and map[1][1] == "O" and map[2][2] == "O":
            print(f"Congratulations to {map[0][0]}!")
            break
        elif map[0][2] == "X" and map[1][1] == "X" and map[2][0] == "X" or map[0][2] == "O" and map[1][1] == "O" and map[2][0] == "O":
            print(f"Congratulations to {map[1][1]}!")
            break
x_o()