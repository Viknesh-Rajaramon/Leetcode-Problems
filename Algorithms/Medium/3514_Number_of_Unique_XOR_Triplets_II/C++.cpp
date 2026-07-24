class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        unordered_set<int> pairs = {0}, triplets(nums.begin(), nums.end());
        int k = 1, max_num = *max_element(nums.begin(), nums.end());
        while (k <= max_num)
            k <<= 1;
        
        while (!nums.empty()) {
            int num = nums.back();
            nums.pop_back();
            for (int x: pairs)
                triplets.insert(num ^ x);
            
            for (int x: nums)
                pairs.insert(num ^ x);
            
            if (triplets.size() == k)
                return k;
        }

        return triplets.size();
    }
};
