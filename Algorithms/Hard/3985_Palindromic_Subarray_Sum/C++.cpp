class Solution {
    struct Node {
        int len, link;
        unordered_map<int, int> next;
    };

public:
    long long getSum(vector<int>& nums) {
        int n = nums.size();
        vector<long long> prefix(n+1);
        for (int i = 0; i < n; ++i)
            prefix[i+1] = prefix[i] + nums[i];
        
        long long result = LLONG_MIN;
        int last = 0;
        vector<Node> tree = {{0, 1}, {-1, 1}};

        auto walk = [&](int node, int i) {
            while (i-1-tree[node].len < 0 || nums[i-1-tree[node].len] != nums[i])
                node = tree[node].link;
            
            return node;
        };

        for (int i = 0; i < n; ++i) {
            int curr = walk(last, i);
            if (!tree[curr].next.count(nums[i])) {
                int link = walk(tree[curr].link, i), len = tree[curr].len+2;
                tree.push_back({len, tree[curr].len == -1 ? 0 : tree[link].next[nums[i]]});
                tree[curr].next[nums[i]] = tree.size()-1;
                result = max(result, prefix[i+1] - prefix[i+1-len]);
            }

            last = tree[curr].next[nums[i]];
        }

        return result;
    }
};
