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
