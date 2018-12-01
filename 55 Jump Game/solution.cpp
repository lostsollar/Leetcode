class Solution {
public:
    bool canJump(vector<int>& nums) {
        int length = nums.size();
        int reach = 0;
        for(int i = 0; i <= reach && i < length; i++)
            reach = max(nums[i] + i, reach);
        return reach >= length - 1;
    }
};
