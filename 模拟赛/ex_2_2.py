def paperFolding(paper_info):
    length = paper_info[0]
    width = paper_info[1]

    result = []

    edge = hcf(length, width)
    result.append(edge)
    result.append(int(length*width/(edge*edge)))

    return result


def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


if __name__ == '__main__':
    paper_info = [7, 3]
    print(paperFolding(paper_info))
