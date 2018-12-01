class Solution {
public:
    int jump(vector<int>& nums) {
        int jumps = 0;
        int curReach = 0;
        int curMax = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (curReach < i) {
                jumps++;
                curReach = curMax;
            }    
            curMax = max(curMax, nums[i] + i);
        }
        return jumps;
    }
};
