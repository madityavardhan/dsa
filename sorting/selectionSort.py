def selectionSort(nums):
    # select minimum and place at the start of the array

    for i in range(len(nums)):
        min_index = i
        for j in range(i,len(nums)):
            if nums[j]<nums[min_index]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index], nums[i]
    return nums

# Main function
nums = [1,3,89,2,1,3,23,2]
print(selectionSort(nums))
