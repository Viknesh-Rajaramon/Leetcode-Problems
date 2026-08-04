class Solution {
public:
    string stoneGameIII(vector<int>& stoneValue) {
        int s1 = 0, s2 = 0, s3 = 0, tot = 0;
        for (int i = stoneValue.size()-1; i >= 0; --i) {
            tot += stoneValue[i];
            int curr = tot - min({s1, s2, s3});
            s3 = s2;
            s2 = s1;
            s1 = curr;
        }

        if (2*s1 > tot)
            return "Alice";
        else if (2*s1 < tot)
            return "Bob";
        
        return "Tie";
    }
};
