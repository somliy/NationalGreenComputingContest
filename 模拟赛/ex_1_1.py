class Task:
    def getSum(self, num1, num2):
        sum = 0
        for i in range(num1, num2 + 1):
            while (i != 0):
                sum += i % 10
                i /= 10
                i = int(i)
        return sum


if __name__ == '__main__':
    task = Task
    a = task.getSum(task, 15, 19)
    print(a)
