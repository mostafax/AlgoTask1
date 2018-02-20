from Quick_Sort import QuickSort
from InsertionSort import Insertion_sort
import time
import random
RequaredRanges = [100000]
#RequaredRanges = [10, 100, 500, 1000, 100000, 500000, 1000000, 10000000]
index = 0
def WriteNumbersinFile(n):
    global index
    Randomied = []
    #Generating Random Numbers
    Number = n[index]
    Write = open("Numbers.txt",'a')
    #Write.write(str(Number)+" ")
    for x in range(0,Number):
        if x<Number-1:
         Write.write((str(random.randint(1,1000))+" "))
        else:
            Write.write((str(random.randint(1, 1000))))
    if index==8:
     index=0
    else:index+=1

def HatMenFile():
    x = open("Numbers.txt", 'r')

    for Number in x:
        Number
    Sub= Number.split(" ")

    #print(Sub)
    x.close()
    return Sub


WriteNumbersinFile(RequaredRanges)

for x in range(0, 1):
        print("QuickSort")
        print(RequaredRanges[x])
        t3 = time.time()

        QuickSort(HatMenFile())
        t4 = time.time() - t3
        print(t4)

        print("Insertions Sort")
        print(RequaredRanges[x])
        t1 = time.time()
        print(Insertion_sort(HatMenFile()))
        t2 = time.time() - t1
        print(t2)


