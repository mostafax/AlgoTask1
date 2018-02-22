import sys
sys.setrecursionlimit(2000)

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])
    out = []
    li = ri = 0  # index of next element from left, right halves
    while True:
        if li >= len(left):  # left half is exhausted
            out.extend(right[ri:])
            break
        if ri >= len(right): # right half is exhausted
            out.extend(left[li:])
            break
        if left[li] < right[ri]:
            out.append(left[li])
            li += 1
        else:
            out.append(right[ri])
            ri += 1
    return out