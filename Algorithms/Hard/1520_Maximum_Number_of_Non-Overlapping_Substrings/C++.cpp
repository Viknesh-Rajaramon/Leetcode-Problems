class Solution {
public:
    vector<string> maxNumOfSubstrings(string s) {
        unordered_map<char, int> counts, first, last;
        vector<char> keys;
        for (int i = 0; i < s.length(); ++i) {
            char c = s[i];
            if (counts.find(c) == counts.end()) {
                counts[c] = 0;
                first[c] = i;
                keys.push_back(c);
            }

            ++counts[c];
            last[c] = i;
        }

        vector<string> result;
        deque<vector<int>> queue;
        for (int k : keys) {
            queue.push_front(vector<int>{first[k], last[k], counts[k]});
            int l = INT_MAX, r = INT_MIN, total = 0;
            for (int i = 0; i < queue.size(); ++i) {
                total += queue[i][2];
                l = min(l, queue[i][0]);
                r = max(r, queue[i][1]);
                if (total == r-l+1)
                    break;
            }

            if (total == r-l+1) {
                result.push_back(s.substr(l, r-l+1));
                queue.clear();
            }
        }

        return result;
    }
};
