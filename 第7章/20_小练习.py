# 学生管理系统
#
# ⚠️ 和 Java 的区别：
#   - 没有 private，属性随便访问
#   - 没有 new，直接类名()
#   - 没有重载，用默认值
#   - 不需要声明属性类型

class Student:
    count = 0
    def __init__(self, name, age):
        Student.count += 1
        self.name = name
        self.age = age
        self.scores = {}
    def add_score(self, subject, score):
        self.scores[subject] = score
    def __str__(self):
        return f'{self.name}: {self.scores}'

class Manager:
    def __init__(self):
        self.students = []
    def add(self):
        name = input('姓名：')
        age = int(input('年龄：'))
        self.students.append(Student(name, age))
    def show(self):
        for s in self.students:
            print(s)
    def run(self):
        while True:
            cmd = input('1添加 2查看 3退出：')
            if cmd == '1': self.add()
            elif cmd == '2': self.show()
            elif cmd == '3': break

Manager().run()
