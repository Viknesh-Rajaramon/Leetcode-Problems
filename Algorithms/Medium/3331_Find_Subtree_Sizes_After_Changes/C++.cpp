class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        vector<vector<int>> children(s.length());
        for (int x = 1; x < s.length(); ++x)
            children[parent[x]].push_back(x);
        
        vector<int> result(s.length(), 1);
        unordered_map<char, int> last;
        function<void(int)> dfs = [&](int x) {
            char c = s[x];
            int above = last.count(c) ? last[c] : -1;
            last[c] = x;
            for (int child : children[x])
                dfs(child);
            
            last[c] = above;
            if (x > 0)
                result[above >= 0 ? above : parent[x]] += result[x];
        };

        dfs(0);
        return result;
    }
};
