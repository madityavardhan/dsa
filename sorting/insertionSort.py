# insertion sort algorithm 
from typing import List
def insertionSort(nums:List[int]) -> List[int]:
    i = 1
    while i < len(nums):
        j = i
        while j>0 and nums[j]<nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j-=1
        i+=1
    return nums
nums = [5,1,6,1,4,7]
print(insertionSort(nums))