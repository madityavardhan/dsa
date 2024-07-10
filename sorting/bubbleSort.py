def bubbleSort(nums):
    # check adjecent elemnts and put the bigger number at the last at every iteration
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [6,2,52,1,1]
print(bubbleSort(nums))