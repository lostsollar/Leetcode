class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        int i = 0;
        int valley = 0;
        int peak = 0;
        int max_profit = 0;
        while (i < length - 1) {
            while (i < length - 1 && prices[i] >= prices[i+1])
                i++;
            valley = prices[i];
            while (i < length - 1 && prices[i] <= prices[i+1])
                i++;
            peak = prices[i];
            
            max_profit += peak - valley;
        }
        return max_profit;
    }
};
