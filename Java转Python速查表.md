# Java 转 Python 速查表

> 你是 Java 老手，这张表就是你的"翻译词典"。
> 左边 Java 怎么写，右边 Python 怎么写，忘了就翻这页。

---

## 一、基础语法

| 你在 Java 里写 | Python 里写 | 备注 |
|---|---|---|
| `int a = 10;` | `a = 10` | 不用声明类型，动态推断 |
| `String name = "张三";` | `name = "张三"` | 同上 |
| `final int MAX = 100;` | `MAX = 100` | 全大写只是约定，技术上能改 |
| `true / false` | `True / False` | **首字母大写！** |
| `null` | `None` | **首字母大写！是个对象** |
| `// 注释` | `# 注释` | |
| `/* 多行 */` | `""" 多行 """` | |
| `if (a > b) { ... }` | `if a > b: ...` | 没括号，有冒号，**缩进代替大括号** |
| `else if` | `elif` | |
| `for (int i = 0; i < 10; i++)` | `for i in range(10):` | 遍历式，不是 C 风格 |
| `while (n < 10) { n++; }` | `while n < 10: n += 1` | 没有 `n++` |
| `a && b` | `a and b` | 用单词 |
| `a \|\| b` | `a or b` | |
| `!a` | `not a` | |
| `a == b`（比地址） | `a == b`（比内容） | **Python 的 == 比内容！比地址用 `is`** |
| `a.equals(b)` | `a == b` | Python 直接 == |

---

## 二、方法/函数

| Java | Python |
|---|---|
| `public void hello() {}` | `def hello():` |
| `public int add(int a, int b)` | `def add(a: int, b: int) -> int:` |
| 方法重载（同名不同参） | **没有重载！用默认值** |
| `return a, b;` 要写个类或数组 | `return a, b` 自动打包元组 |
| 可变参数 `int... nums` | `*args`（元组） |
| 只能按顺序传参 | `greet(name="张三", age=18)` 关键字传参 |

---

## 三、面向对象

| Java | Python |
|---|---|
| `new Person("张三")` | `Person("张三")` **没有 new！** |
| `class Student extends Person` | `class Student(Person)` |
| `super(name, age)` | `super().__init__(name, age)` |
| `private String name;` | `self.__name`（改名，不是真私有） |
| `protected String name;` | `self._name`（约定） |
| `static int count = 0;` | 类里直接写 `count = 0` |
| `@Override` | 直接写同名方法 |
| `toString()` | `__str__()` |
| `equals()` | `__eq__()` |
| `instanceof` | `isinstance()` |
| `Math.abs()` | `abs()` 内置函数 |

---

## 四、集合

| Java | Python |
|---|---|
| `ArrayList<Integer> list = new ArrayList<>();` | `nums = [10, 20, 30]` |
| `list.add(1)` | `nums.append(1)` |
| `list.get(0)` | `nums[0]` |
| `list.size()` | `len(nums)` |
| `list.remove(0)` | `nums.pop(0)` 或 `nums.remove(10)` |
| `Set<String> set = new HashSet<>();` | `s = {"a", "b"}` |
| `Map<String,Integer> map = new HashMap<>();` | `d = {"张三": 72}` |
| `map.put("a", 1)` | `d["a"] = 1` |
| `map.get("a")` | `d["a"]` |
| `map.keySet()` | `d.keys()` |
| `map.entrySet()` 遍历 | `for k, v in d.items():` |

---

## 五、异常

| Java | Python |
|---|---|
| `try { ... } catch (Exception e) {}` | `try: ... except Exception:` |
| `finally {}` | `finally:` |
| `throw new Exception("错")` | `raise Exception("错")` |
| `class MyException extends Exception` | `class MyError(Exception): pass` |

---

## 六、Java 里没有的 Python 特性

这些是你最容易"硬套 Java"结果踩坑的地方：

| 特性 | 说明 |
|---|---|
| **切片** | `nums[1:4]` `nums[::-1]` 反转 |
| **列表推导式** | `[n*2 for n in nums if n > 0]` |
| **lambda** | `lambda a, b: a + b` |
| **装饰器** | `@log` 给函数加功能 |
| **多返回值** | `return a, b` 自动元组 |
| **解包** | `a, b, c = [1, 2, 3]` |
| ***args/**kwargs** | 可变参数打包 |
| **字典推导** | `{k: v for ...}` |
| **三元表达式** | `s = "成年" if age >= 18 else "未成年"` |
| **多继承** | `class C(A, B):` |

---

## 七、最容易踩的 10 个坑

1. **不要写两个 `__init__`** → Python 没有重载，后面的覆盖前面的
2. **不要写 `new`** → 直接 `Person()`
3. **`True/False/None` 首字母大写**
4. **`==` 比内容，`is` 比地址** → 字符串比较用 `==`
5. **缩进是语法** → 不是风格，错了就报错
6. **列表/字典传参是引用传递** → 函数里改了外面也变
7. **没有 `n++`** → 用 `n += 1`
8. **整数除法 `/` 永远得小数** → 取整用 `//`
9. **Python 没有 `do-while`**
10. **GIL 锁** → 多线程不是真正并行，CPU 密集用多进程

---

## 八、并发

| Java | Python |
|---|---|
| `new Thread(r).start()` | `Thread(target=func).start()` |
| `ExecutorService` | `ThreadPoolExecutor` |
| `synchronized` | `Lock()` / `with lock:` |
| `Thread.join()` | `thread.join()` |
| `setDaemon(true)` | `daemon = True` |
| **多线程真正并行** | **GIL 锁，同一时刻只有一个线程执行** |
| CPU 密集用线程池 | CPU 密集用**多进程** |
