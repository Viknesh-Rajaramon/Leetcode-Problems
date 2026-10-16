class BIT {
public:
    int size;
    unordered_map<int, long long> tree_1, tree_2;

    BIT(int n) {
        size = n;
    }

    void add(int l, int r, int delta) {
        _add(l, delta);
        _add(r+1, -delta);
    }

    long long query(int l, int r) {
        return _query(r) - _query(l-1);
    }

private:
    void _add(int idx, int delta) {
        ++idx;
        long long i = idx;
        while (idx <= size) {
            tree_1[idx] += delta;
            tree_2[idx] += (i - 1) * delta;
            idx += idx & -idx;
        }
    }

    long long _query(int idx) {
        ++idx;
        if (idx > size)
            idx = size;

        long long res = 0, i = idx;
        while (idx > 0) {
            res += i*tree_1[idx] - tree_2[idx];
            idx -= idx & -idx;
        }

        return res;
    }
};

class Solution {
public:
    int sumCounts(vector<int>& nums) {
        long result = 0, curr = 0;
        int n = nums.size(), mod = 1e9+7;
        BIT bit(n+10);
        unordered_map<int, int> seen;
        for (int i = 0; i < n; ++i) {
            int j = (seen.count(nums[i]) ? seen[nums[i]] : -1) + 1;
            curr = (curr + 2LL * bit.query(j, i) + i - j + 1) % mod;
            result = (result + curr) % mod;
            bit.add(j, i, 1);
            seen[nums[i]] = i;
        }

        return result;
    }
};
