class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(),nums.end());
        int res=0;
        for(auto i:numSet){
            if(numSet.find(i-1)==numSet.end()){
                int curMax=1;
                while(numSet.find(i+1)!=numSet.end()){
                    i++;
                    curMax++;
                }
                res=max(res,curMax);
            }
        }
        return res;
    }
};