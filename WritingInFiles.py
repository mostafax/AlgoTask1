from Quick_Sort import QuickSort
from InsertionSort import Insertion_sort
from BubleSort import bubble_sort
from Selection_Sort import selection_sort
import sys
from Merge_Sort import merge_sort
import time
import random
RequaredRanges = [10000000]
#RequaredRanges = [10, 100, 500, 1000,10000,100000, 500000, 1000000, 10000000]
index = 0

def WriteNumbersinFileSmall(n):
    global index
    Randomied = []
    #Generating Random Numbers
    Number = n[index]
    Write = open("Small_Numbers.txt",'a')
    Write.write(str(Number)+"\n")
    for x in range(0,Number):
        if x<Number-1:
         Write.write((str(random.randint(1,10000))+" "))
        else:
            Write.write((str(random.randint(1, 10000)))+"\n")
    if index==8:
     index=0
    else:index+=1

def WriteNumbersinFileBig(n):
    global index
    Randomied = []
    #Generating Random Numbers
    Number = n[index]
    Write = open("VLargeNumbers.txt",'a')
    Write.write(str(Number)+"\n")
    for x in range(0,Number):
        if x<Number-1:
         Write.write((str(random.randint(1,10000))+" "))
        else:
            Write.write((str(random.randint(1, 10000)))+"\n")
    if index==8:
     index=0
    else:index+=1



def HatMenFile():
    x = open("Small_Numbers.txt", 'r')

    for Number in x:
        Number
    Sub= Number.split(" ")
    x.close()
    return Sub




#WriteNumbersinFileSmall(RequaredRanges)
WriteNumbersinFileBig(RequaredRanges)
#fes = HatMenFile()
#es  = HatMenFile()

MG = HatMenFile()
AK = MG
for x in range(0, 1):
        WriteResult = open("Result.txt" ,"a")

        WriteResult.write("QuickSort\n")
        WriteResult.write(str(RequaredRanges[x])+'\n')
        t3 = time.time()

        #QuickSort(AK)
        t4 = time.time() - t3
        WriteResult.write(str(t4)+'\n')

        WriteResult.write("MergeSort\n")
        WriteResult.write(str(RequaredRanges[x])+'\n')
        T4 = time.time()
        #merge_sort(MG)
        T7 = time.time()-T4
        WriteResult.write(str(T7)+'\n')

