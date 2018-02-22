from Quick_Sort import QuickSort
from InsertionSort import Insertion_sort
from BubleSort import bubble_sort
import time
import random
RequaredRanges = [10000]
#RequaredRangesSmall = [10, 100, 500, 1000,10000,100000, 500000, 1000000, 10000000]
index = 0
def WriteNumbersinFile(n):
    global index
    Randomied = []
    #Generating Random Numbers
    Number = n[index]
    Write = open("Small_Numbers.txt",'a')
    #Write.write(str(Number)+" ")
    for x in range(0,Number):
        if x<Number-1:
         Write.write((str(random.randint(1,10000))+" "))
        else:
            Write.write((str(random.randint(1, 10000))))
    if index==8:
     index=0
    else:index+=1

def HatMenFile():
    x = open("Small_Numbers.txt", 'r')

    for Number in x:
        Number
    Sub= Number.split(" ")

    #print(Sub)
    x.close()
    return Sub


WriteNumbersinFile(RequaredRanges)
fes = HatMenFile()
es  = HatMenFile()
bs= HatMenFile()
for x in range(0, 1):
        WriteResult = open("Result.txt" ,"w")

        WriteResult.write("QuickSort\n")
        WriteResult.write(str(RequaredRanges[x])+'\n')
        t3 = time.time()

        QuickSort(fes)
        t4 = time.time() - t3
        WriteResult.write(str(t4)+'\n')

        WriteResult.write("Buble Sort"+'\n')
        WriteResult.write(str(RequaredRanges[x])+'\n')
        t5 = time.time()
        bubble_sort(bs)
        t6 = time.time() - t5
        WriteResult.write(str(t6)+'\n')


        WriteResult.write("Insertions Sort\n")
        WriteResult.write(str(RequaredRanges[x])+'\n')
        t1 = time.time()
        Insertion_sort(es)
        t2 = time.time() - t1
        WriteResult.write(str(t2)+'\n')

