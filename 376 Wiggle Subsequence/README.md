方案1: 思路很简单, 每次比较相邻的两个数, 看他们的差值与上一个差值是否是相同性质的数字(同正或同负), 如果性质不同, 则结果加一; 否则比较下一对相邻的数字. 如注意一些特殊情况, 比如只有两个数字并且相同, 例如[5, 5], 此时结果为1, 与只有一个数字时相同.

方案2、3: 参考「Solution」中的 linear dynamic programming