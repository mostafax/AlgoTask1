def SelectionSort(SortList): 
 for i in range(len(SortList)):

    # Find the minimum element in remSortListining 
    # unsorted SortList
    min_idx = i
    for j in range(i + 1, len(SortList)):
        if SortList[min_idx] > SortList[j]:
            min_idx = j

    # SwSortListp the found minimum element with 
    # the first element        
    SortList[i], SortList[min_idx] = SortList[min_idx], SortList[i]
 return SortList