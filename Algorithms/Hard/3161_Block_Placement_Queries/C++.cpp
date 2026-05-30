class Solution {
public:
    vector<int> seg;

    void update(int idx, int val, int p, int l, int r) {
        if (l == r) {
            seg[p] = val;
            return;
        }

        int mid = (l+r) >> 1;
        if (idx <= mid)
            update(idx, val, p << 1, l, mid);
        else
            update(idx, val, p << 1 | 1, mid+1, r);
        
        seg[p] = max(seg[p << 1], seg[p << 1 | 1]);
    }

    int query(int L, int R, int p, int l, int r) {
        if (L <= l && r <= R)
            return seg[p];
        
        int mid = (l+r) >> 1, res = 0;
        if (L <= mid)
            res = max(res, query(L, R, p << 1, l, mid));
        
        if (R > mid)
            res = max(res, query(L, R, p << 1 | 1, mid+1, r));

        return res;
    }

    vector<bool> getResults(vector<vector<int>>& queries) {
        int n = min<int>(50000, queries.size()*3);
        seg.resize(n << 2);
        set<int> st = {0, n};
        update(n, n, 1, 0, n);
        vector<bool> result;
        for (auto &q : queries){
            if (q[0] == 1) {
                int x = q[1];
                auto it = st.upper_bound(x);
                int l = *prev(it), r = *it;
                update(x, x-l, 1, 0, n);
                update(r, r-x, 1, 0, n);
                st.insert(x);
            } else {
                int x = q[1], sz = q[2];
                auto it = st.upper_bound(x);
                int pre = *(--it);
                result.push_back(max(x-pre, query(0, pre, 1, 0, n)) >= sz);
            }
        }

        return result;
    }
};
