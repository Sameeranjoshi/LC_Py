from errno import EACCES
import random


def main():
    print("Hello, String!")
    somestr = "This is a string with spaces and some special characters like \n and \t"
    print(somestr)
    print(somestr[0:20])
    somestr += " and some more characters appended" # THIS IS A NEW STRING AND NOT THE SAME OBJECT ABOVE how to check that?
    print(somestr)
    # Extract words from the string
    words = somestr.split()
    print(words)


    # somestr[0:10] = "That was a typo" # Mutation not allowed in string
    # print(somestr)

    print(str(int(1) + int(2)))
    print(int("1") + int("2"))
    print(int(1) + int(2))
    print(str(1) + str(2))

    listofstr = ["sam", "amir", "saurabh", "manasij"]
    newlist = []
    print(listofstr)
    for eachstr in listofstr:
        print(eachstr)
        newlist.append(eachstr)
    print(listofstr)
    print(newlist)


    # let's joing now.
    print("POP".join(listofstr))


    str1 = "sam"
    str2 = "amir"

    print(str1 + str2)
    print(str1)
    print(str2)

    print(str1[2])
    print(str1[-2])
    print(str1[0:2])
 

    somestring = "This is a string with a repeating word called a which is a word"
    somestring = somestring.replace("a", "SAM")
    print(somestring)
    print("Tell me length of string: ", len(somestring))

    somestring = somestring.upper()
    print(somestring)
    somestring = somestring.lower()
    print(somestring)

    somestring += "       "
    somestring = "       " + somestring
    print(somestring)
    
    print(somestring.strip())
    
    a = "amir"
    s = "sam"
    print(f"a: {a}, s: {s}")
    aplus_s = a + " " + s
    print(f"aplus_s: {aplus_s}")

    repeat = a * 3
    print(f"repeat: {repeat}")
    name = "Alice"
    surname = "Bob"
    age = 20
    print(f"name: {name}, surname: {surname}, age: {age}")
    ss = "name {}, surname: {}, age: {}".format(name, surname, age)
    print(f"ss: {ss}")

    if "dam" in aplus_s:
        print("sam found")
    else:
        print("sam not found")

if __name__ == "__main__":
    main()