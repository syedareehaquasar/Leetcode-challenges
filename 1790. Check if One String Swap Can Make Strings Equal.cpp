class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        vector<int> unequal;
        for (int i = 0; i < s1.size(); i++){
            if (s1[i] != s2[i]) unequal.push_back(i);
        }
        if (unequal.empty()) return true;
        if (unequal.size() != 2) return false;
        if (s1[unequal[0]] == s2[unequal[1]] && s1[unequal[1]] == s2[unequal[0]]) return true;
        return false;
    }
};
