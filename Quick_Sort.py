def QuickSort(Array):
    DoQuickSort(Array,0,len(Array)-1)

    return Array


def DoQuickSort(Array,first,last):
   if first<last:

       splitpoint = partition(Array,first,last)

       DoQuickSort(Array,first,splitpoint-1)
       DoQuickSort(Array,splitpoint+1,last)

# Spliting the Array Function and Returning the The Right pointer
def partition(Array,first,last):
   Pivot = Array[first]

   LeftPointer = first+1
   RightPointer = last

   done = False
   while not done:

       while LeftPointer <= RightPointer and Array[LeftPointer] <= Pivot:
           LeftPointer = LeftPointer + 1

       while Array[RightPointer] >= Pivot and RightPointer >= LeftPointer:
           RightPointer = RightPointer -1

       if RightPointer < LeftPointer:
           done = True
       else:
           temp = Array[LeftPointer]
           Array[LeftPointer] = Array[RightPointer]
           Array[RightPointer] = temp

   temp = Array[first]
   Array[first] = Array[RightPointer]
   Array[RightPointer] = temp


   return RightPointer




