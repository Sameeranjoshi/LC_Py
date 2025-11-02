# various data structures
# dict, set, hashmap, tuple, Queue, maps, heaps, 

def tuple():
    mytuple = (1,2,3,4,5,4)
    print(mytuple)
    # what are difference between tuple and list?
    # show some examples operations on tuple
    print(mytuple.count(4))
    print(mytuple.index(4))
    print(len(mytuple))
    print(mytuple + (6,7,8,9,10))
    print(mytuple * 3)
    print(mytuple[0])
    print(mytuple[0:3])

def setexample():
    print("set:\n")
    myset = {1,2,3, 3, -100}
    myanotherset = {-1, -2, -3, -100}
    print(myset)
    print(myanotherset)

    # index ? not possible because it's not ordered and might be stored in hash table, so...
    # print(myset[3])
    if -1 in myset:
        print("2 is in myset")
    else:
        print("2 is not in myset")

    # mathematical algebra can be applied on sets.
    unionset = myset.union(myanotherset)
    print(unionset)
    #intersection of 2 sets
    intersectionset = myset.intersection(myanotherset)
    print(intersectionset)
    differenceset = myanotherset.difference(myset)
    print(differenceset)


    # some other operations on sets
    myset.add(3)
    myset.add(2)
    myset.add(99)
    print(myset)

    myset.remove(99)
    print(myset)
    myset.remove(2)
    print(myset)

    print(f"length of myset: {len(myset)}")

    difftypeset = {1, "sam", 10.3, True}
    print(difftypeset)
    difftypeset.add(10.3)
    difftypeset.add("sameeran")
    print(difftypeset)
    print(type(difftypeset))

    setofemployees = {"sam", "sameeran", "saurabh", "amit"}
    print("sameeran" in setofemployees)
    print("sameeran" not in setofemployees)

    my_list_with_duplicates = [10, 20, 30, 10, 40, 50, 20, 60, 30]
    my_unique_set = set(my_list_with_duplicates)

    print(f"Original List: {my_list_with_duplicates}")
    print(f"Resulting Set: {my_unique_set}")


    # 
    mynewset = {1,2,3,3}
    mynewset.add(4)  # add
    mynewset.remove(3) # remove
    print(2 in mynewset) # find
    

# dict is nothing but hashmap and is like set, just a key value set and can be modified.
def dictexample():
    print("dictionary:\n\n")
    # extension of set but you can modify it along with key.
    # set(tuple(key value))

    mydict = {
        1:"sameeran",
        2:"amir",
        3:"saurabh",
        4:"amit",
        1:"repeatsameeran"
    }
    mydict[1] = "newsameeran"
    mydict[10] = "newvalue"
    # To remove a key from a dictionary, use the del statement or the pop() method:
    del mydict[4]
    # alternatively:
    # mydict.pop(4)
    print(mydict)

    # add, remove and check

    for key, value in mydict.items():
        print(f" key: {key}, value: {value}")
    for index, value in enumerate(mydict.items()):
        print(f"index: {index}, value: {value}")

    # check if element present in dictionary
    for key, value in mydict.items():
        if value == "amir":
            print(f"amir is in the dictionary")
    print("sudhir" in mydict.values())
    print(1 in mydict.keys())
    # unlike set you can modify elements


    dict2 = {}
    dict2["alice"] = 100
    dict2["bob"] = 200
    dict2["charlie"] = 300
    dict2["dave"] = 400
    dict2["eve"] = 500
    print(dict2)
    print("alice" in dict2)

if __name__ == "__main__":
    # tuple
    tuple()
    setexample()
    dictexample()
    # tuple list, dict, set are builtin data structures in python