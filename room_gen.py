import random

def rand_map():
    map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def up(map, i, j):
        map[i - 1][j] = 1
        
    def down(map, i, j):
        map[i + 1][j] = 1

    def left(map, i, j):
        map[i][j - 1] = 1

    def right(map, i, j):
        map[i][j + 1] = 1

    for z in range(5):
        for i in range(0, 10):
            for j in range(0, 10):
                if map[i][j] == 1:
                    func = random.choice([0, 1, 2, 3])
                    if i == 0 and j == 0:
                        if func == 1:
                            right(map, i, j)

                        elif func == 2:
                            left(map, i, j)
                        break

                    elif i == 0 and j == 9:
                        if func == 2:
                            left(map, i, j)

                        elif func == 3:
                            down(map, i, j)
                        break

                    elif i == 9 and j == 9:
                        if func == 0:
                            up(map, i, j)

                        elif func == 2:
                            left(map, i, j)
                        break

                    elif i == 9 and j == 0:
                        if func == 0:
                            up(map, i, j)

                        elif func == 1:
                            right(map, i, j)
                        break

                    elif i == 0:

                        if func == 1:
                            right(map, i, j)

                        elif func == 2:
                            left(map, i, j)

                        elif func == 3:
                            down(map, i, j)
                        break

                    elif i == 9:
                        if func == 0:
                            up(map, i, j)

                        elif func == 1:
                            right(map, i, j)

                        elif func == 2:
                            left(map, i, j)
                        break

                    elif j == 0:
                        if func == 0:
                            up(map, i, j)

                        elif func == 1:
                            right(map, i, j)

                        elif func == 3:
                            down(map, i, j)
                        break

                    elif j == 9:
                        if func == 0:
                            up(map, i, j)
                
                        elif func == 2:
                            left(map, i, j)
                            
                        elif func == 3:
                            down(map, i, j)
                        break

                    else:
                        if func == 0:
                            up(map, i, j)

                        elif func == 1:
                            right(map, i, j)

                        elif func == 2:
                            left(map, i, j)

                        elif func == 3:
                            down(map, i, j)
                        break


    # for i in range(10):
    #     print(map[i])

    return map

