class Solution {
public:
    int totalNumbers(vector<int>& digits) {
        vector<int> freq(10);
        for (int d : digits)
            ++freq[d];

        int result = 0;
        for (int i = 1; i < 10; ++i) {
            if (freq[i] == 0)
                continue;

            --freq[i];
            for (int j = 0; j < 10; ++j) {
                if (freq[j] == 0)
                    continue;
                    
                --freq[j];
                for (int k = 0; k < 10; k += 2) {
                    if (freq[k] == 0)
                        continue;
                    
                    ++result;
                }    
                
                ++freq[j];
            }

            ++freq[i];
        }
        
        return result;
    }
};
