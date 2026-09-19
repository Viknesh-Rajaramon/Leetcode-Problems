class Solution {
public:
    vector<int> countTasks(vector<int>& tasks, vector<int>& shifts) {
        function<int(vector<long long>&, long long)> bisect_right = [&](vector<long long>& arr, long long x) {
            int low = 0, high = arr.size();
            while (low <= high) {
                int mid = (low + high) >> 1;
                if (arr[mid] <= x)
                    low = mid+1;
                else
                    high = mid-1;
            }

            return low;
        };
        
        int n = tasks.size();
        vector<long long> arr(n, 0);
        arr[0] = tasks[0];
        for (int i = 1; i < n; ++i)
            arr[i] += arr[i-1] + tasks[i];
        
        vector<int> result;
        long long total = arr[n-1], carry = 0;
        for (int shift : shifts) {
            carry += shift;
            if (carry >= total) {
                result.push_back(0);
                carry = 0;
            } else {
                result.push_back(n - bisect_right(arr, carry));
            }
        }

        return result;
    }
};
