import os, sys


class Task:
    def showDirTree(self, path):
        print("+--" + path.split('\\')[-1])
        for dir in os.listdir(path):
            if os.path.isdir(path):
                print(" " * 2 + "+--" + dir)
                self.dealDir(task,path + "\\" + dir, 4)
            else:
                print(" " * 2 + "--" + dir)

    def dealDir(self, path, step):
        if (os.listdir(path) != None):
            for dir in os.listdir(path):
                new_path = path + "\\" + dir
                if os.path.isdir(new_path):
                    print(" " * step + "+--" + dir)
                    self.dealDir(self, path + "\\" + dir, step + 2)
                else:
                    print(" " * step + "--" + dir)


if __name__ == '__main__':
    path = "C:\\Users\\486\\Desktop\\test\\root"
    task = Task
    task.showDirTree(task, path)
