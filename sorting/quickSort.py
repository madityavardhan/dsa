from typing import List
def quickSort(nums:List[int]) -> List[int]:
    # base case with single element
    if len(nums)<2:
        return nums
    # Select a pivot element, Last element in this case
    pivotElement = nums[-1]
    # move all elements less than the pivot to left
    leftArray = [num for num in nums[:-1] if num <= pivotElement]  
    # All elements greater than pivot to right of it
    rightArray = [num for num in nums[:-1] if num > pivotElement] 
    # recursively sort left and right arrays 
    return quickSort(leftArray) + [pivotElement] + quickSort(rightArray)
if __name__ == '__main__':
    nums = [5,2,62,45]
    print(quickSort(nums))