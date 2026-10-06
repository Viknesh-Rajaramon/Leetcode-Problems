class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> result;
        map<int, int> freq;
        for (int num : nums)
            ++freq[num];
        
        while (!freq.empty()) {
            for (auto it = freq.begin(); it != freq.end(); ) {
                result.push_back(it->first);
                it->second--;
                if (it->second == 0)
                    it = freq.erase(it);
                else
                    it++;
            }
        }
        
        return result;
    }
};
