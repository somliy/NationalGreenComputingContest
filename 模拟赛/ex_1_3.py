import os, sys


class Task:
    def showDirTree(self, path):
        print("+--" + path.split('\\')[-1])
        for dir in os.listdir(path):

            if os.path.isdir(path + "\\" + dir):
                print(" " * 2 + "+--" + dir)
                self.dealDir(task, path + "\\" + dir, 4)
            else:
                if (self.judge(self, dir)):
                    print(" " * 2 + "--" + dir)

    def dealDir(self, path, step):
        if os.path.isfile(path):
            if (self.judge(self, os.path.basename(path))):
                print(" " * step + "--" + os.path.basename(path))
        else:
            if (os.listdir(path) != None):
                for dir in os.listdir(path):
                    new_path = path + "\\" + dir

                    if os.path.isdir(new_path):
                        print(" " * step + "+--" + dir)
                        self.dealDir(self, path + "\\" + dir, step + 2)
                    else:
                        if (task.judge(self, dir)):
                            print(" " * step + "--" + dir)

    def judge(self, dir):
        if os.path.splitext(dir)[1] == ".jpg" or os.path.splitext(dir)[1] == ".png" or os.path.splitext(dir)[
            1] == ".bmp":
            return True
        else:
            return False


if __name__ == '__main__':
    path = "C:\\Users\\486\\Desktop\\test\\dir"
    task = Task

    task.showDirTree(task, path)
