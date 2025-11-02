def main():
    # basic data types
    var = 100
    floatingvar = 10.3
    stringvar = "sam is sam"
    boolvar = True
    print(f"var: {var}, floatingvar: {floatingvar}, stringvar: {stringvar}, boolvar: {boolvar}")

    # advance data types
    # list, tuple, dictionary, set
    Iamlist = [1,2,3,4,5, 2]
    Iamlist2 = ["sam", 1, 10.3, True] # kind of struct
    Iamlist3 = ["amir", 2, 1.3, False] # another emulated struct
    Iamlist4 = ["saurabh", 3, 100.3, True]
    Iamlist5 = [Iamlist2, Iamlist3, Iamlist4, Iamlist4]
    Iammanuallyconstructedlist = list((10,  20.3))
    Iamrepeatedlist = [100, 10.2] * 10
    # what are properties of list? 
    # 1. ordered
    # 2. mutable
    # 3. can contain duplicates
    # 4. can be nested
    # 5. can be indexed
    # 6. can be sliced
    # 7. can be concatenated
    # 8. can be repeated
    # 9. can be sorted

    print(f"Iamlist: {Iamlist}")
    print(f"Iamlist2: {Iamlist2}") # doesn't have to have same type of elements
    print(f"Iamlist3: {Iamlist3}") # can be nested
    print(f"Iamlist4: {Iamlist4}") # can be nested
    print(f"Iamlist5: {Iamlist5}") # can be nested
    print(f"Iammanuallyconstructedlist: {Iammanuallyconstructedlist}")
    print(f"Iamrepeatedlist: {Iamrepeatedlist}")
    Iamlist[0] = 1000
    Iamlist5[1][2] = 1000
    print(f"After modification:")
    print(f"Iamlist: {Iamlist}")
    print(f"Iamlist5: {Iamlist5}")

    # play with it various operations
    Iamlist2.append(Iamlist3)
    print(f"Iamlist2: {Iamlist2}")
    Iamlist2.append("sameeran")
    print(f"Iamlist2: {Iamlist2}")
    Iamlist2.insert(3, "sameeraninserted")
    print(f"Iamlist2: {Iamlist2}")

    # access list 
    print(f"Iamlist3: {Iamlist3}")
    Iamlist3[0] = "sam"
    Iamlist3[-1] = "sameeran"
    print(f"Iamlist3: {Iamlist3}")


    # shallow copy list
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    Iamlistshallowcopy = [list1, list2[:]]
    print(f"Iamlistshallowcopy: {Iamlistshallowcopy}")
    Iamlistshallowcopy[0][0] = 1000
    Iamlistshallowcopy[1][0] = 1000
    print(f"Iamlistshallowcopy: {Iamlistshallowcopy}")
    print(f"list1: {list1}")
    print(f"list2:, {list2}")
    Iamlistshallowcopy.clear()
    print(f"Iamlistshallowcopy: {Iamlistshallowcopy}")
    list1.remove(4)
    del list1[0]
    print(f"list1: {list1}")


    # iterate or access list and not modify.
    for element in list1:
        print(f"element: {element}")
    for index, element in enumerate(list1):
        print(f"index: {index}, element: {element}")

    # matrix from a list using nested
    matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
    print(f"matrix: {matrix}")
    matrix[0][0] = 1000
    print(f"matrix: {matrix}")
    

    print(f"list1: {list1}")
    newlist = [element*2 for element in list1]
    print(f"newlist: {newlist}")
    list10 = [100, 10, 20, 30, 30, 40, 50, 60, 30, 30, 40]
    print(list10.count(30))
    list10.sort()
    print(f"list10: {list10}")
    list10.reverse()
    print(f"list10: {list10}")



    somelist = [1, 2, 3, 4, 5]
    print(somelist)
    somelist.append(6)
    print(somelist)
    somelist.remove(3)
    print(somelist)
    somelist.reverse()
    print(somelist)
    for element in somelist:
        print(element)
    for index, element in enumerate(somelist):
        print(f"index: {index}, element: {element}")
    somelist.reverse()
    somelist.insert(2, 3)   # O(n) time
    print(somelist)
    for element in range(len(somelist), 0, -1):
        print(element)
    
    # lsit as stack
    somelist.append(6) # push
    print(somelist)
    somelist.pop()
    print(somelist)
    somelist.pop()
    print(somelist)
    somelist.pop()
    print(somelist)
    somelist.pop()
    print(somelist)
    somelist.pop() # pop
    print(somelist)
    somelist.pop() # pop
    print(somelist)
    somelist.pop() # pop
    print(somelist)

    somelist.extend([1,2,3,4,5,6])
    print(somelist)

    #slicing
    print(somelist[0:2])
    # more slicing examples
    print(somelist[0:2])
    print(somelist[0:len(somelist):2])
    print(somelist[1:len(somelist):2])

    a, b, c = somelist[3:6]
    print(f"a: {a}, b: {b}, c: {c}")

    evenindex = somelist[::2]
    oddindex = somelist[1::2]
    print(f"evenindex: {evenindex}, \n oddindex: {oddindex}")

    for even, odd in zip(evenindex, oddindex):
        print(f"even: {even}, odd: {odd}")

    print(somelist)
    somelist.sort(reverse=True)
    print(somelist)

    # comprehension is to initize lists
    anotherlist = [i - 1 for i in somelist]
    print(anotherlist)
    
    

if __name__ == "__main__":
    main()