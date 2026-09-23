class Solution {
public:
    int maximumGap(string skill, string station) {
        int m = station.size(), n = skill.size(), i = 0;
        vector<int> left(n), right(n);
        for (int j = 0; j < n; ++j) {
            while (i < m && station[i] != skill[j])
                ++i;

            left[j] = i++;
        }
        
        i = m-1;
        for (int j = n-1; j >= 0; --j) {
            while (i >= 0 && station[i] != skill[j])
                --i;
            
            right[j] = i--;
        }
        
        int result = 0;
        for (int i = 0; i < n-1; ++i)
            result = max(result, right[i+1] - left[i]);

        return result;
    }
};
