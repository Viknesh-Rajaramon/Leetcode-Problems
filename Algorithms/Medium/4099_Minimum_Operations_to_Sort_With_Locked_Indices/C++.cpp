class FenwickTree {
private:
    int n;
    vector<int> bit;

public:
    FenwickTree(int n) : n(n), bit(n+1) {}

    void update(int idx, int val) {
        while (idx <= n) {
            bit[idx] += val;
            idx += idx & -idx;
        }
    }

    int query(int idx) {
        int res = 0;
        while (idx > 0) {
            res += bit[idx];
            idx -= idx & -idx;
        }

        return res;
    }
};

class Solution {
public:
    int minOperations(vector<int>& nums, vector<int>& locked, int k) {
        int n = nums.size(), start = 0, max_so_far = 0;
        vector<vector<int>> blocks;
        for (int i = 0; i < n; ++i) {
            max_so_far = max(max_so_far, nums[i]);
            if (max_so_far == i+1) {
                blocks.push_back({start, i});
                start = i+1;
            }
        }
        
        int result = 0;
        for (vector<int>& block : blocks) {
            int start = block[0], end = block[1];
            if (start == end)
                continue;
            
            for (int i = start; i <= end; ++i)
                if (locked[i] == 1)
                    ++result;
        }
                    
        if (result > k)
            return -1;
            
        FenwickTree ft(n);
        for (int i = n-1; i >= 0; --i) {
            result += ft.query(nums[i]-1);
            ft.update(nums[i], 1);
        }
        
        return result;
    }
};
