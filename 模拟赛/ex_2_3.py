def countOfShips(ferry):
    result = 0
    mp = [([0] * len(ferry[0])) for p in range(len(ferry))]
    # for i in range(len(ferry)):
    #     for j in range(len(ferry[0])):
    #         print(mp[i][j], end='')
    #     print()
    for i in range(len(ferry)):
        for j in range(len(ferry[0])):
            if (ferry[i][j] == "+"):
                # print(i, j)
                result += 1
                if (judge(i + 1, j, ferry) or (judge(i - 1, j, ferry)) or (judge(i, j + 1, ferry)) or (judge(i, j - 1, ferry))):
                    # print(judge(i + 1, j, ferry) , (judge(i - 1, j, ferry)) , (judge(i, j + 1, ferry)) , (judge(i, j - 1, ferry)))
                    if (judges(i + 1, j, mp) or (judges(i - 1, j, mp)) or (judges(i, j + 1, mp)) or (judges(i, j - 1, mp))):
                        # print(judges(i + 1, j, mp) , (judges(i - 1, j, mp)) , (judges(i, j + 1, mp)) , (judges(i, j - 1, mp)))
                        result -= 1
                        # print(i, j)

                mp[i][j] = 1

    return result


def judge(x, y, ferry):
    l = len(ferry)
    w = len(ferry[0])
    if (x < 0 or x >= l or y < 0 or y >= w): return False
    if (ferry[x][y] == "+"):
        return True;
    else:
        return False;


def judges(x, y, mp):
    l = len(mp)
    w = len(mp[0])
    if (x < 0 or x >= l or y < 0 or y >= w): return False
    if (mp[x][y] == 1):
        return True;
    else:
        return False;


if __name__ == '__main__':
    ferry = [
        ["+", "o", "o", "+", "o"],
        ["o", "o", "o", "o", "+"],
        ["o", "+", "o", "o", "+"],
        ["o", "+", "o", "o", "+"]
    ]
    print(countOfShips(ferry))

