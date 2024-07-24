class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        // //in-built function
        // next_permutation(nums.begin(),nums.end());
        
        // find the break point 
        int breakPoint=-1;
        for(int i=nums.size()-1;i>0;i--){
            if(nums[i]>nums[i-1]){
                breakPoint=i-1;
                break;
            }
        }
        if(breakPoint==-1){
            reverse(nums.begin(),nums.end());
            return;
        }
        // swap it with the next larget element
        int curLarge=breakPoint+1;
        for(int i=breakPoint+1;i<nums.size();i++){
            if(nums[i]>nums[breakPoint] && nums[i]<=nums[curLarge]){
                curLarge=i;
            }
        }
        swap(nums[breakPoint],nums[curLarge]);
        // reverse the remaining array
        reverse(nums.begin()+breakPoint+1,nums.end());
    }
};