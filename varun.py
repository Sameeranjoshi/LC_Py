# # datastructutes
# # list, tuple, dictionary, set


# import time


# def maketea(ingredients:dict):
#     # hot milk + tea + chocolate=no == hot tea
#     # cold milk + tea + chocolate=no == cold tea
#     # hot milk + coffee + chocolate=no == hot coffee
#     # cold milk + coffee + chocolate=no == cold coffee
#     # milk=hot + chocolate=yes == hot chocolate
#     # milk=cold + chocolate=yes == cold chocolate


#     if ingredients["milk"] == "hot" and ingredients["beans"] == "tea" and ingredients["chocolate"] == "no":
#         print("hot tea")
#     elif ingredients["milk"] == "cold" and ingredients["beans"] == "tea" and ingredients["chocolate"] == "no":
#         print("cold tea")
#     elif ingredients["milk"] == "hot" and ingredients["beans"] == "coffee" and ingredients["chocolate"] == "no":
#         print("hot coffee")
#     elif ingredients["milk"] == "cold" and ingredients["beans"] == "coffee" and ingredients["chocolate"] == "no":
#         print("cold coffee")
#     elif ingredients["milk"] == "hot" and ingredients["chocolate"] == "yes":
#         print("hot chocolate")
#     elif ingredients["milk"] == "cold" and ingredients["chocolate"] == "yes":
#         print("cold chocolate")
#     else:
#         print("Invalid ingredients")
    



# if __name__ == "__main__":
#     # print("Varun's code")
#     # milk = [hot/cold]
#     # beans = [tea/coffee]
#     # sugar = [brown/white]
#     # chocolate = [yes/no]
    
#     somedatastructure = {}
#     somedatastructure["milk"] = "hot"
#     somedatastructure["beans"] = "coffee"
#     somedatastructure["chocolate"] = "jokip"

#     # maketea(somedatastructure)
#     # print(output_ingredients)


#     SIZEOFLIST = 1000000000

#     # list
#     elements = [88] * SIZEOFLIST
#     elements[SIZEOFLIST - 1] = 17

#     starttime = time.time()
#     if 17 in elements:
#         print("17 is in the list")
#     endtime = time.time()
#     print(f"time taken LIST: {endtime - starttime}")


#     # dict
#     mydict = {}
#     for i in range(SIZEOFLIST):
#         mydict[i] = 88
#     mydict[SIZEOFLIST - 1] = 17


#     starttime = time.time()
#     if 17 in mydict:
#         print("17 is in the dict")
#     endtime = time.time()
#     print(f"time taken DICT: {endtime - starttime}")


import time

N = 100000000  # 1 million (pick something realistic)

# list: O(n)
lst = [88] * N
lst[-1] = 17


t0 = time.perf_counter()
print(17 in lst)
t1 = time.perf_counter()
print(f"list membership time: {t1 - t0:.6f}s")

# set: O(1) average
st = {88, 17}  # you don't need N copies in a set (duplicates collapse)

t0 = time.perf_counter()
print(17 in st)
t1 = time.perf_counter()
print(f"set membership time: {t1 - t0:.6f}s")
