class Solution(object):
    # myself
    def isSubsequence1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length_s = len(s)
        length_t = len(t)
        i = 0
        j = 0
        while i < length_s and j < length_t:
            while j < length_t and i < length_s and t[j] != s[i]:
                j += 1
            if j < length_t and i < length_s and t[j] == s[i]:
                i += 1
                j += 1

        return i == length_s    

    # more concise
    def isSubsequence2(self, s, t):
        length_s = len(s)
        length_t = len(t)
        i = 0
        j = 0
        while i < length_s and j < length_t:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == length_s
