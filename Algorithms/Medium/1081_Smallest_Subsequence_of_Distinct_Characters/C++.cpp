class Solution {
public:
    string smallestSubsequence(string s) {
        set<char> visited;
        unordered_map<char, int> freq;
        for (char c: s) {
            if (freq.find(c) == freq.end())
                freq[c] = 0;
            
            ++freq[c];
        }

        string result;
        for (char c: s) {
            --freq[c];
            if (visited.count(c))
                continue;
            
            while (!result.empty() && result.back() > c && freq[result.back()] > 0) {
                visited.erase(result.back());
                result.pop_back();
            }

            result.push_back(c);
            visited.insert(c);
        }

        return result;
    }
};
