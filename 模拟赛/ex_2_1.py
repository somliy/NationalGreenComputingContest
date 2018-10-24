def dailyTemps(temp_list):
    result = []

    for ca in range(0, len(temp_list)-1):
        for i in range(ca + 1, len(temp_list)):
            ind = temp_list[ca]
            flag = 0
            if (temp_list[i] > ind):
                result.append(i - ca)
                flag = 1
                break
        if (flag == 0):
            result.append(0)

    result.append(0)
    return result


if __name__ == '__main__':
    temp_list = [1,3,2]
    print(dailyTemps(temp_list))
