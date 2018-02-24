#(selection_sort) function on list returen the sorted version of it.

def selection_sort(a):
    sort_len=0               #length of current sorted portion.
    while sort_len<len(a):
        min_idx=None         #index of smallest item found.
        for i,elem in enumerate(a[sort_len:]):
            if min_idx==None or elem<a[min_idx]:          #check if current element is the smallest
                min_idx=i+sort_len                        #update with current smallest
        a[sort_len],a[min_idx]=a[min_idx],a[sort_len]
        sort_len+=1
    return a
