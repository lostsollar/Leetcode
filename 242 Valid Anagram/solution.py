# -*- coding:utf-8 -*-
class Solution(object):

    def isAnagram(self, s, t):
        """
        My solution, Accepted[可以排序，但是时间复杂度比这个高]
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True
        length_s = len(s)
        length_t = len(t)
        if length_s != length_t:
            return False

        s_dict = {}
        for i in range(length_s):
            s_dict.setdefault(s[i], 0)
            s_dict[s[i]] += 1
        for i in range(length_t):
            if t[i] not in s_dict:
                return False
            else:
                if s_dict[t[i]] == 1:
                    del s_dict[t[i]]
                else:
                    s_dict[t[i]] -= 1
        return True

    def isAnagram1(self, s, t):
        dict1, dict2 = {}, {}
        for item in s:
            dict1[item] = dict1.get(item, 0) + 1
        for item in t:
            dict1[item] = dict2.get(item, 0) + 1
        return dict1 == dict2

    def isAnagram2(self, s, t):
        list1, list2 = [0] * 26, [0] * 26
        for item in s:
            list1[ord(item) - ord('a')] += 1
        for item in t:
            list2[ord(item) - ord('a')] += 1
        return list1 == list2

    def isAnagram3(self, s, t):
        return sorted(s) == sorted(t)


checker = Solution()
s = "anagram"
t = "nagaram"
s1 = "cat"
t1 = "tac"
print checker.isAnagram2(s1, t1)
