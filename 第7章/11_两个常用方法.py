# isinstance / issubclass
#
# ⚠️ Java vs Python 差异：
#   Java：instanceof 关键字
#   Python：isinstance(obj, Class) 函数

class Person: pass
class Student(Person): pass

s = Student()

print(isinstance(s, Student))   # 相当于 Java 的 s instanceof Student
print(issubclass(Student, Person))  # 判断是不是子类
