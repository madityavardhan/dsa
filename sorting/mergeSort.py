# merge sort algotithm 
from typing import List
def mergeSort(nums:List[int]) -> List[int]:
    l, r = 0, len(nums)-1
    mid = (l+r)//2
    mergeSort(nums[l:mid+1])
    mergeSort(nums[mid+1:r])
    
# Main
nums = [2,41,51,5,1]
nums = mergeSort(nums)
print(nums)

