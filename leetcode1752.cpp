class Solution {
public:
    bool check(vector<int>& nums) {
        int j=0, n=nums.size();
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i]>nums[i+1]) j++;
        }
        if(nums[n-1]>nums[0]) j++;
        return j>1?false:true;
    }
};