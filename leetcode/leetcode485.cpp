class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int curMax=0,res=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==1) curMax++;
            else curMax=0;
            res=max(res,curMax);
        }
        return res;
    }
};