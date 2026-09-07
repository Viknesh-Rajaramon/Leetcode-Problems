class Solution {
public:
    vector<string> result;

    void dfs(string prev, int cost, string path, int n, int k) {
        if (cost > k)
            return;
        
        if (path.length() == n) {
            result.push_back(path);
            return;
        }

        dfs("0", cost, path+"0", n, k);
        if (prev != "1")
            dfs("1", cost+path.length(), path+"1", n, k);
    }

    vector<string> generateValidStrings(int n, int k) {
        dfs("0", 0, "", n, k);
        return result;
    }
};
