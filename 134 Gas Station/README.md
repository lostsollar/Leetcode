## 134 Gas Station

#### 解题的两点原因：

1.如果总的 gas 比总的 cost 要大，那么一定存在一个解。并且题目描述里保证了解是唯一的，那么第一个正确的解就是答案

2.tank 永远不应该为负，因此如果 tank 为负，就从下一个结点重新开始，并让 tank = 0

#### c++
```cpp
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int sumGas = 0;
        int sumCost = 0;
        int tank = 0;
        int start = 0;
        for (int i=0; i<gas.size(); i++) {
            sumGas += gas[i];
            sumCost += cost[i];
            tank += gas[i] - cost[i];
            if (tank < 0) {
                start = i + 1;
                tank = 0; 
            }
        }
        
        return sumGas < sumCost ? -1 : start;
    }
};
```
#### python

```python
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sum_gas = 0
        sum_cost = 0
        start = 0
        tank = 0
        for i in range(len(gas)):
            sum_gas += gas[i]
            sum_cost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return -1 if sum_gas < sum_cost else start
```
