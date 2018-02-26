from Quick_Sort import QuickSort
from InsertionSort import Insertion_sort
from BubleSort import bubble_sort
from Selection_Sort import selection_sort
import sys
from Merge_Sort import merge_sort
from time import time
import random
from ReadingFromFiles import HatMenFileSmall , HatMenFileBig , HatMenFileVBig
from WritingInFiles import WriteNumbersinFileBig , WriteNumbersinFileVBig,Generate_to_100000

RequaredRanges = [10, 100, 500, 1000,10000,100000]
RequaredRangesBig = [ 1000000, 10000000]

#Generate_to_100000() #Done
#WriteNumbersinFileBig() #Done 1000000
#WriteNumbersinFileVBig() #Done 10000000

SmallHat=HatMenFileSmall()

#Doing all from 1 To 100000
for x in range(0,6):
    Result_File = open("Result.txt","a")
    #QuickSort
    Result_File.write("QuickSort\n")
    Result_File.write(str(RequaredRanges[x])+'\n')
    TForQuick1 =time()
    QuickSort(SmallHat[x])
    TForQuick2 = time()-TForQuick1
    Result_File.write(str(TForQuick2)+"\n")

    Result_File.write("MergeSort\n")
    Result_File.write(str(RequaredRanges[x])+'\n')
    TForQuick1 =time()
    merge_sort(SmallHat[x])
    TForQuick2 = time()-TForQuick1
    Result_File.write(str(TForQuick2)+"\n")

    Result_File.write("SelectionSort\n")
    Result_File.write(str(RequaredRanges[x])+'\n')
    TForQuick1 =time()
    selection_sort(SmallHat[x])
    TForQuick2 = time()-TForQuick1
    Result_File.write(str(TForQuick2)+"\n")

    Result_File.write("InsertionSort\n")
    Result_File.write(str(RequaredRanges[x])+'\n')
    TForQuick1 =time()
    Insertion_sort(SmallHat[x])
    TForQuick2 = time()-TForQuick1
    Result_File.write(str(TForQuick2)+"\n")

    Result_File.write("BubleSort\n")
    Result_File.write(str(RequaredRanges[x])+'\n')
    TForQuick1 =time()
    bubble_sort(SmallHat[x])
    TForQuick2 = time()-TForQuick1
    Result_File.write(str(TForQuick2)+"\n")

MeduimHat= HatMenFileBig()
BigHat= HatMenFileVBig()

#Doing all from  1000000 To 100000000
Result_File = open("Result.txt", "a")
# QuickSort
Result_File.write("QuickSort\n")
Result_File.write(str(RequaredRangesBig[0]) + '\n')
TForQuick1 = time()
QuickSort(MeduimHat)
TForQuick2 = time() - TForQuick1
Result_File.write(str(TForQuick2) + "\n")


# MERGE sORT
Result_File.write("MergeSort\n")
Result_File.write(str(RequaredRangesBig[0]) + '\n')
TForQuick1 = time()
merge_sort(MeduimHat)
TForQuick2 = time() - TForQuick1
Result_File.write(str(TForQuick2) + "\n")

Result_File.write("QuickSort\n")
Result_File.write(str(RequaredRangesBig[1]) + '\n')
TForQuick1 = time()
QuickSort(BigHat)
TForQuick2 = time() - TForQuick1
Result_File.write(str(TForQuick2) + "\n")


# MERGE sORT
Result_File.write("MergeSort\n")
Result_File.write(str(RequaredRangesBig[1]) + '\n')
TForQuick1 = time()
merge_sort(BigHat)
TForQuick2 = time() - TForQuick1
Result_File.write(str(TForQuick2) + "\n")



