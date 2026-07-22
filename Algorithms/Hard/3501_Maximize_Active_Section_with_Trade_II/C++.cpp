class SparseTable {
private:
    vector<vector<int>> st;

public:
    SparseTable(const vector<int> &data) {
        st.push_back(data);
        int i = 1, n = st[0].size();
        while (2*i <= n+1) {
            const auto& pre = st.back();
            vector<int> curr;
            for (int j = 0; j <= n-2*i; ++j)
                curr.push_back(max(pre[j], pre[j+i]));
            
            st.push_back(curr);
            i <<= 1;
        }
    }

    int query(int begin, int end) {
        if (begin > end)
            return 0;
        
        int len = end-begin+1;
        int lg = 0;
        while ((1 << (lg+1)) <= len)
            ++lg;
        
        return max(st[lg][begin], st[lg][end+1-(1<<lg)]);
    }
};

class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.size(), cnt = count(s.begin(), s.end(), '1'), i = 0;
        vector<int> zero_blocks, left, right;
        while (i < n) {
            int st = i;
            while (i < n && s[i] == s[st])
                ++i;
            
            if (s[st] == '0') {
                zero_blocks.push_back(i-st);
                left.push_back(st);
                right.push_back(i-1);
            }
        }

        int m = zero_blocks.size();
        if (m < 2)
            return vector<int>(queries.size(), cnt);

        vector<int> tmp_sum(m-1);
        for (int i = 0; i < m-1; ++i)
            tmp_sum[i] = zero_blocks[i] + zero_blocks[i+1];
        
        SparseTable st(tmp_sum);

        vector<int> result;
        for (const auto& q: queries) {
            int i = lower_bound(right.begin(), right.end(), q[0]) - right.begin();
            int j = upper_bound(left.begin(), left.end(), q[1]) - left.begin() - 1;

            if (i > m-1 || j < 0 || i >= j) {
                result.push_back(cnt);
                continue;
            }

            int first = right[i]+1-max(left[i], q[0]), last = min(right[j], q[1])+1-left[j];
            if (i+1 == j) {
                result.push_back(cnt+first+last);
                continue;
            }

            int best = max({first+zero_blocks[i+1], zero_blocks[j-1]+last, st.query(i+1, j-2)});
            result.push_back(cnt+best);
        }

        return result;
    }
};
