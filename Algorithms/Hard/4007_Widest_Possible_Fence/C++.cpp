class Solution {
public:
    int maximumWidth(vector<int>& planks) {
        unordered_map<int, int> freq, height;
        vector<int> values;
        for (int plank : planks) {
            if (freq.find(plank) == freq.end())
                freq[plank] = 0;
            
            ++freq[plank];
        }
        
        for (auto& [key, _] : freq) {
            height[key] = freq[key];
            values.push_back(key);
        }
        
        int n = values.size();
        for (int i = 0; i < n; ++i) {
            int a = values[i];
            for (int j = i; j < n; ++j) {
                int b = values[j];
                int h = a+b;
                if (height.find(h) == height.end())
                    height[h] = 0;
                
                height[h] += (a == b ? freq[a] / 2 : min(freq[a], freq[b]));
            }
        }
        
        int result = 0;
        for (auto& [h, _] : height)
            result = max(result, height[h]);
        
        return result;
    }
};
