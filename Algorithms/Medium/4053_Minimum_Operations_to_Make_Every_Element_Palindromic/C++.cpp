class Solution {
public:
    long long minOperations(vector<int>& nums) {
        static vector<long long> even, odd;
        if (even.empty()) {
            for(int i = 1; i <= 10; ++i) {
                int h = (i+1)/2;
                long long l = 1;
                for(int j = 1; j < h ; ++j)
                    l *= 10;
                
                for(long long j = l; j < l*10; ++j) {
                    string x = to_string(j), y = x;
                    int m = x.size();
                    for(int k = (i%2 ? m-2 : m-1); k >= 0; --k)
                        y += x[k];
                    
                    long long v = stoll(y);
                    if(v%2==0)
                        even.push_back(v);
                    else
                        odd.push_back(v);
                }
            }

            sort(even.begin(), even.end());
            sort(odd.begin(), odd.end());
        }

        long long result = 0;
        for(int num : nums) {
            vector<long long>& arr = (num%2) ? odd : even;
            int j = lower_bound(arr.begin(), arr.end(), (long long)num) - arr.begin();
            long long best = LLONG_MAX;
            if(j < arr.size())
                best = arr[j] - num;
            
            if(j > 0 && num - arr[j-1] < best)
                best = num - arr[j-1];
            
            result += best/2;
        }
        
        return result;
    }
};
