# statements, loops, expressions, functions, classes, objects, modules
# in python examples

# class
class dummyclass:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter and setters
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}"


def class_example():
    name_age_list = [("sam", 20), ("amir", 21), ("saurabh", 22)] # list of tuples
    for name, age in name_age_list:
        U = dummyclass(name, age)
        print(U)

def loops():    
    i = 0
    while i < 10:
        print(i)
        i += 1

def statements():
    print("Statements:")

    # assignment statement
    a, b = 1, 2
    # looping statements
    for i in range(10):
        print(i)
    # conditional statements
    if a > b: 
        print("a is greater than b")
    elif a < b:
        print("a is less than b")
    else:
        print("a is equal to b")
    
    # switch statement
    match a:
        case 1:
            print("a is 1")
        case 2:
            print("a is 2")    
        case _:
            print("a is not 1 or 2")
    # import statements
    import math
    # return statements

    # pass statements
    # break statements
    # continue statements
    for i in range(10):
        if i == 5:
            pass
        elif i == 2:
            continue
        elif i == 8:
            break
        else:
            print(i)

    # raise statements
    try:
        raise Exception("This is a test exception")
    except Exception as e:
        print(e)

    # except statements
    # finally statements
    try:
        # import sameeranlib
        c = a / 0
    except Exception as e:
        print(e)
    finally:
        print("finally block")
    


def expressions():
    print("Expressions:")
    a = 1
    b = 2

    # arithmetic expressions
    c = a + b
    d = a / b # float division
    e = a // b # integer division
    f = a % b 
    g = a ** 2
    print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}, f: {f}, g: {g}")

    # logican expressions(input: boolean, output: boolean)
    h = a and b # logical and
    i = a or b # logical or
    j = not a # logical not
    print(f"h: {h}, i: {i}, j: {j}")

    # relational expressions(inpit: int, float, output: boolean
    k = a < b 
    l = a == b 
    m = a != b
    print(f"k: {k}, l: {l}, m: {m}")
    

def functions(a, b):
    print("Functions:")
    def add():
        return a + b
    print(add())    # can access the external variables a and b
    # print(add(1, 2))

    # lambda functions
    # lambda arguments: expression
    somelambda_function = lambda a, b: a + b
    print(somelambda_function(1000, 2000))

def modules_example():
    import math
    print(math.sqrt(16))

    import random
    print(random.randint(1, 100))

    import datetime
    print(datetime.datetime.now())

if __name__ == "__main__":
    
    class_example()
    loops()
    expressions()
    functions(10, 20)
    modules_example()
    statements()


