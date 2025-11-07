# various data structures
# dict, set, hashmap, tuple, Queue, maps, heaps, 
import math
from typing import Optional, List

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


def dequeexample():
    from collections import deque
    class Q:
        def enque(self, dq, element):
            dq.append(element)
        def dequeue_element(self, dq):
            return dq.popleft()
        def getFront(self, dq):
            return dq[0]
        def getRear(self, dq):
            return dq[-1]
        def size(self, dq):
            return len(dq)        
        def isEmpty(self, dq):
            if self.size(dq) == 0:
                return True
            return False

    print("deque:\n\n")
    # add elements
    dq = deque()
    qq = Q()
    qq.enque(dq, 10)
    qq.enque(dq, 20)
    qq.enque(dq, 30)
    print(dq)

    qq.dequeue_element(dq)
    print(dq)
    qq.dequeue_element(dq)
    print(dq)

    print(qq.getFront(dq))
    print(qq.getRear(dq))


def treeexamples():

    # Definition for a binary tree node.
    import math
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    class Solution:
        def dfs(self, root:Optional[TreeNode], listtoadd):
            if root is None:
                return
            listtoadd.append(root.val)
            self.dfs(root.left, listtoadd)
            self.dfs(root.right, listtoadd)

        def bfs(self, root:Optional[TreeNode], listtoadd):
            from collections import deque
            dq = deque()
            dq.append(root)

            while dq:
                newroot = dq.popleft()
                listtoadd.append(newroot.val)
                if newroot.left != None:
                    dq.append(newroot.left)
                if newroot.right != None:
                    dq.append(newroot.right)
            
        def preorderTraversal(self, root: Optional[TreeNode], preorderlist:List[int]) -> List[int]:
            self.dfs(root, preorderlist)

        def sumthetree(self, root):
            if root is None:
                return 0 
            return root.val + self.sumthetree(root.left) + self.sumthetree(root.right)

        def height_tree(self, root):
            if root is None:
                return 0
            return 1 + max(self.height_tree(root.left), self.height_tree(root.right))

        def max_tree(self, root):
            if root is None:
                return -math.inf
            return max(self.max_tree(root.left), self.max_tree(root.right), root.val)
        
        def ispresentintree(self, root, target) -> bool:
            if root is None:
                return False
            if root.val == target: 
                return True
            return self.ispresentintree(root.left, target) or self.ispresentintree(root.right, target)

        def mirrortree(self, root):
            if root is None:
                return
            
            temp = root.left
            root.left = root.right
            root.right = temp

            self.mirrortree(root.left)
            self.mirrortree(root.right)


        def issymmetric(self, root):
            if root is None:
                return
            if root.left and root.right and root.left.val == root.right.val:
                return True
            else:
                return False
            return self.issymmetric(root.left) and self.issymmetric(root.right)

    # A = TreeNode(1)
    # B = TreeNode(2)
    # C = TreeNode(3)
    # A.left, A.right = B, C
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(4)
    """
        1
    2       3

    """

    sol = Solution()
    finallist = []
    # sol.preorderTraversal((root), finallist)
    # print(finallist)

    # bfslist = []
    # sol.bfs(root, bfslist)
    # print(bfslist)


    # sumtree = 0
    # print(sol.sumthetree(root))



    print("Height", sol.height_tree(root))
    print("Max tree", sol.max_tree(root))
    print("Sum tree", sol.sumthetree(root))
    print("is 2 present in tree", sol.ispresentintree(root, 2))

    sol.preorderTraversal((root), finallist)
    print("Before mirror")
    print(finallist)
    finallist = []
    sol.mirrortree(root)
    sol.preorderTraversal((root), finallist)
    print("After mirror")
    print(finallist)


    print("Is symmetric = ", sol.issymmetric(root))
        
if __name__ == "__main__":
    # tuple
    tuple()
    setexample()
    dictexample()
    dequeexample()
    treeexamples()
    # tuple list, dict, set are builtin data structures in python