class Solution {
public:
    int maxJumps(vector<int>& arr, int d) {
        int n = arr.size();
        vector<int> result(n, 1);
        vector<int> stack;

        for (int i = 0; i <= n; ++i) {
            while (stack.size() > 0 && (i == n || arr[stack.back()] < arr[i])) {
                vector<int> indices = {stack.back()};
                stack.pop_back();
                while (stack.size() > 0 && arr[stack.back()] == arr[indices[0]]) {
                    indices.push_back(stack.back());
                    stack.pop_back();
                }

                for (int j : indices) {
                    if (i < n && i-j <= d) {
                        result[i] = max(result[i], result[j]+1);
                    }

                    if (stack.size() > 0 && j-stack.back() <= d) {
                        result[stack.back()] = max(result[stack.back()], result[j]+1);
                    }
                }
            }

            if (i < n)
                stack.push_back(i);
        }

        return *max_element(result.begin(), result.end());
    }
};
