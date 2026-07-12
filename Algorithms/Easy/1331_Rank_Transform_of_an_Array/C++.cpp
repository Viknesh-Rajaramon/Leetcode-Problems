class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        map<int, int> ranks;
        set<int> nums(arr.begin(), arr.end());
        int rank = 1;
        for (int num: nums)
            ranks[num] = rank++;
        
        vector<int> result;
        for (int num: arr)
            result.push_back(ranks[num]);

        return result;
    }
};
