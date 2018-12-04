class Solution {
public:
    bool isSubsequence(string s, string t) {
        int sLen = s.length(), sIdx = 0, tLen = t.length();
        for (int i=0; i<tLen && sIdx<sLen; i++)
            if (s[sIdx] == t[i]) sIdx++;
        return sIdx == sLen;
    }
};
