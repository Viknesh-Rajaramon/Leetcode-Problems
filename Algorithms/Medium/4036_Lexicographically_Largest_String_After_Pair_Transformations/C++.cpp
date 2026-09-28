class Solution {
public:
    vector<string> largestString(vector<int>& nums) {
        vector<string> result;
        for (int num : nums) {
            string curr;
            int z = num / (1 << 25);
            if (z) {
                curr.append(z, 'z');
                num %= (1 << 25);
            }
            
            for (int i = 24; i >= 0; --i)
                if (num & (1 << i))
                    curr += char('a' + i);

            result.push_back(curr);
        }

        return result;
    }
};
