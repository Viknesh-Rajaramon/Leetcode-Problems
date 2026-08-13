class Solution {
public:
    vector<int> longestRepeating(string s, string queryCharacters, vector<int>& queryIndices) {
        int n = s.size();
        vector<int> pre(4*n), suf(4*n), max_len(4*n);
        vector<char> left_char(4*n), right_char(4*n);

        function<void(int, int, int)> push_up = [&](int u, int l, int r) {
            int m = (l + r) >> 1;
		    int left_len = m-l+1, right_len = r-m, left = u << 1, right = u << 1 | 1;
		    left_char[u] = left_char[left];
            right_char[u] = right_char[right];
		    pre[u] = pre[left];
            suf[u] = suf[right];

            if (pre[left] == left_len && right_char[left] == left_char[right])
                pre[u] = pre[left] + pre[right];

            if (suf[right] == right_len && right_char[left] == left_char[right])
                suf[u] = suf[right] + suf[left];

            max_len[u] = max(max_len[left], max_len[right]);
            if (right_char[left] == left_char[right])
                max_len[u] = max(max_len[u], suf[left]+pre[right]);
        };

        function<void(int, int, int)> build = [&](int u, int l, int r) {
            if (l == r) {
			    pre[u] = 1;
                suf[u] = 1;
                max_len[u] = 1;
                left_char[u] = s[l];
                right_char[u] = s[l];
			    return;
		    }

            int m = (l + r) >> 1;
            build(u << 1, l, m);
            build(u << 1 | 1, m+1, r);
            push_up(u, l, r);
        };

        function<void(int, int, int, int, char)> update = [&](int u, int l, int r, int pos, char ch) {
            if (l == r) {
			    left_char[u] = ch;
                right_char[u] = ch;
			    return;
		    }

            int m = (l + r) >> 1;
            if (pos <= m) {
                update(u << 1, l, m, pos, ch);
            } else {
                update(u << 1 | 1, m+1, r, pos, ch);
            }

            push_up(u, l, r);
        };

        build(1, 0, n-1);
        vector<int> result;
        int k = queryIndices.size();
        for (int i = 0; i < k; ++i) {
            update(1, 0, n-1, queryIndices[i], queryCharacters[i]);
            result.push_back(max_len[1]);
        }

        return result;
    }
};
