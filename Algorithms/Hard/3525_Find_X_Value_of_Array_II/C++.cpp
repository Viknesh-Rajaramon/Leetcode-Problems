class SegmentTree {
private:
    static const int MAX_K = 6;
    int k;
    vector<array<int, MAX_K>> tree;

    void make_leaf(int o, int value) {
        tree[o].fill(0);
        int r = value % k;
        tree[o][r] = 1;
        tree[o][k] = r;
    }

    void merge_pre(const array<int, MAX_K>& left, const array<int, MAX_K>& right, array<int, MAX_K>& result) {
        result.fill(0);
        result[k] = (left[k] * right[k]) % k;
        for (int x = 0; x < k; ++x)
            result[x] = left[x];
        
        for (int x = 0; x < k; ++x)
            result[(left[k] * x) % k] += right[x];
    }

    void build(const vector<int>& nums, int o, int l, int r) {
        if (l == r) {
            make_leaf(o, nums[l]);
            return;
        }
            
        int m = (l+r) >> 1;
        build(nums, o << 1, l, m);
        build(nums, (o << 1) | 1, m+1, r);
        merge_pre(tree[o << 1], tree[(o << 1) | 1], tree[o]);
    }

public:
    SegmentTree(vector<int>& nums, int k) : k(k) {
        int n = nums.size();
        tree.resize(2 << (int)ceil(log2(n)));
        build(nums, 1, 0, n-1);
    }

    void update(int o, int l, int r, int index, int value) {
        if (l == r) {
            make_leaf(o, value);
            return;
        }

        int m = (l+r) >> 1;
        if (index <= m)
            update(o << 1, l, m, index, value);
        else
            update((o << 1) | 1, m+1, r, index, value);

        merge_pre(tree[o << 1], tree[(o << 1) | 1], tree[o]);
    }

    array<int, MAX_K> query(int o, int l, int r, int L, int R) {
        if (L <= l && r <= R)
            return tree[o];

        int m = (l+r) >> 1;
        if (R <= m)
            return query(o << 1, l, m, L, R);
        
        if (L > m)
            return query((o << 1) | 1, m+1, r, L, R);

        array<int, MAX_K> left = query(o << 1, l, m, L, R), right = query((o << 1) | 1, m+1, r, L, R), result;
        merge_pre(left, right, result);
        return result;
    }
};

class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        vector<int> result;
        int n = nums.size();
        SegmentTree st(nums, k);
        for (auto& q : queries) {
            int index = q[0], value = q[1], start = q[2], x = q[3];
            st.update(1, 0, n-1, index, value);
            result.push_back(st.query(1, 0, n-1, start, n-1)[x]);
        }

        return result;
    }
};
