class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Dont make it toomuch complicated, 
        if you encounter 0, place it in the front, 
        if 2 place it at the end
        if 1 increment the cur index, since its at the correct place
        """
        i,j,k = 0,0,len(nums)-1
        while j<=k:
            if nums[j] == 0:
                nums[j],nums[i] = nums[i],nums[j]
                i+=1
                j+=1
            elif nums[j]==1:
                j+=1
            else:
                nums[j],nums[k] = nums[k],nums[j]
                k-=1