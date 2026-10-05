class Solution {
public:
    vector<int> largestPower(vector<int>& nums) {
        vector<int> result;
        vector<vector<int>> old_temp = {nums};
        for (int bit = 14; bit >= 0; --bit) {
            int mask = 1 << bit, count = 0;
            bool splitting = true;
            vector<vector<int>> new_temp;
            for (vector<int>& section : old_temp) {
                if (splitting) {
                    vector<int> section_0, section_1;
                    for (int num : section) {
                        if (num & mask)
                            section_1.push_back(num);
                        else
                            section_0.push_back(num);
                    }
                    
                    if (section_1.size() > 0) {
                        count += section_1.size();
                        new_temp.push_back(section_1);
                    }
                    
                    if (section_0.size() > 0) {
                        splitting = false;
                        new_temp.push_back(section_0);
                    }
                } else {
                    new_temp.push_back(section);
                }
            }
            
            result.push_back(count);
            old_temp = new_temp;
        }

        return result;
    }
};
