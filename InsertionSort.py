import time

def Insertion_sort(nums):

  for x in range(1,len(nums)):
    value = nums[x]
    temp=x
    while (temp > 0) and (nums[temp-1] > value):
      nums[temp]=nums[temp-1]
      temp=temp-1

    nums[temp]=value
  return nums

