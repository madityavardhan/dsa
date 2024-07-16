class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n=nums.size();
        if(n<=1) return;
        // while(k--){
        //     // swap last element to 1st (Gives TLE)
        //     for(int i=n-1;i>0;i--){
        //         swap(nums[i],nums[i-1]);
        //     }
        // }

        // 1,2,3,4,5,6,7 -> 7,6,5,4,3,2,1 -> 5,6,7,1,2,3,4
        reverse(nums.begin(),nums.end());
        reverse(nums.begin(),nums.begin()+(k%n));
        reverse(nums.begin()+(k%n),nums.end());
    }
};