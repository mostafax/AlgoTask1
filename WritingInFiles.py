from Quick_Sort import QuickSort
from InsertionSort import Insertion_sort
from BubleSort import bubble_sort
from Selection_Sort import selection_sort
import sys
from Merge_Sort import merge_sort
import time
import random
from ReadingFromFiles import HatMenFileSmall
#RequaredRanges = [10000000]
RequaredRanges = [10, 100, 500, 1000,10000,100000]
RequaredRangesBig = [ 1000000, 10000000]
index = 0
indexBig =0

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

def WriteNumbersinFileBig():

    #Generating Random Numbers
    Number = 1000000
    Write = open("LargeNumbers.txt",'a')
    Write.write(str(Number)+"\n")
    for x in range(0,Number):
        if x<Number-1:
         Write.write((str(random.randint(1,10000))+" "))
        else:
            Write.write((str(random.randint(1, 10000)))+"\n")


def WriteNumbersinFileVBig():

    #Generating Random Numbers
    Number = 10000000
    Write = open("VLargeNumbers.txt",'a')
    Write.write(str(Number)+"\n")
    for x in range(0,Number):
        if x<Number-1:
         Write.write((str(random.randint(1,10000))+" "))
        else:
            Write.write((str(random.randint(1, 10000)))+"\n")








#WriteNumbersinFileSmall(RequaredRanges)

#fes = HatMenFile()
#es  = HatMenFile()

def Generate_to_100000():
  for x in range(0, 6):
        WriteNumbersinFileSmall(RequaredRanges)


#Generate_to_100000() #Done
#WriteNumbersinFileBig() #Done
#WriteNumbersinFileVBig() #Done

