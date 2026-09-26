# isinstance判断实例类型，issubclass判断子类
class Person: pass
class Student(Person): pass

s = Student()

# isinstance(对象, 类)：判断对象是不是某类（或子类）的实例
print(isinstance(s, Student))   # True
print(isinstance(s, Person))   # True

# issubclass(类1, 类2)：判断类1是不是类2的子类
print(issubclass(Student, Person))  # True
