# code for various patterns
# 1. Sliding Window
# 2. Two-Pointer
# 3. Slow and Fast Pointers
# 4. Reversing a Linked List in Place
# 5. Binary Search
# 6. Top K Elements (Heaps)
# 7. Binary Tree Traversal
# 8. Graphs and Matrices
# 9. Backtracking
# 10. Dynamic Programming
# 11. Bit Manipulation
# 12. Overlapping Intervals
# 13. Prefix Sums

# sliding window over a list
def longestsubstring(inputstring: str):
    # longest substring without duplicates
    myset = set()
    finalmap = dict()
    st = 0
    end = 0
    maxlength = 0
    longeststring = ""
    for index, ch in enumerate(inputstring):
        if ch in myset:
            length = len(myset)
            substring = inputstring[st:end]
            if length > maxlength:
                maxlength = length
                longeststring = substring
            myset.clear()
            st = end
        myset.add(ch)
        end += 1

    print(longeststring)
    print(maxlength)

def sumtotarget(target, listofnumbers):
    print("\nsum to target")
    m = {}
    for elem in listofnumbers:
        m[elem] = elem

    for eachelem in listofnumbers:
        diff = target - eachelem
        if diff in m:
            print(f"found: {eachelem}")

def dosomething(list1):
    print("\ndosomething")

    newlist = []
    counter = 0
    for elem in list1:
        if elem is not 0:
            newlist.append(elem)
        else:
            counter += 1

    print(f"counter: {counter}")
    print(f"newlist: {newlist}")
    while counter > 0:
        newlist.append(0)
        counter -= 1
    return newlist



if __name__ == "__main__":
    print("\nlongest substring without duplicates")
    longestsubstring("abcabcbb")
    longestsubstring("bbbbb")
    longestsubstring("pwwkew")


    # problem 2
    target = 9
    listofnumbers = [2, 7, 11, 15]
    sumtotarget(target, listofnumbers)

    # # problem 3 
    list1 = [1, 0 , 2, 0 , 4, 6]
    newlist = dosomething(list1)
    print(newlist)


