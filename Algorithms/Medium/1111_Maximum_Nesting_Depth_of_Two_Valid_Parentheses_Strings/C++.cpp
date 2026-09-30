class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        vector<int> result;
        for (int i = 0; i < seq.length(); ++i) {
            if (seq[i] == '(')
                result.push_back(i%2);
            else
                result.push_back(1 - i%2);
        }

        return result;
    }
};
