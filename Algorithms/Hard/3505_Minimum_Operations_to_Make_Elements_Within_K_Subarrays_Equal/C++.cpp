class Solution {
public:
    long long minOperations(vector<int>& nums, int x, int k) {
        int n = nums.size(), l_size = x/2, r_size = x - x/2;
        vector<pair<int, int>> init;
        for (int i = 0; i < x; ++i)
            init.push_back({nums[i], i});
        
        sort(init.begin(), init.end());
        int mid = init[l_size].first;
        priority_queue<pair<int, int>> left;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> right;
        long long cost = 0;
        for (int j = 0; j < x; ++j) {
            auto [num, i] = init[j];
            cost += abs(num - mid);
            if (j < l_size)
                left.push({num, i});
            else
                right.push({num, i});
        }

        vector<long long> costs(x, LLONG_MAX);
        costs.push_back(cost);
        for (int i = x; i < n; ++i) {
            cost += abs(nums[i] - mid) - abs(nums[i-x] - mid);
            if (nums[i-x] < right.top().first || (nums[i-x] == right.top().first && i-x < right.top().second)) {
                while (!left.empty() && -left.top().second <= i-x)
                    left.pop();
                
                if (nums[i] < right.top().first) {
                    left.push({nums[i], i});
                } else {
                    auto [pop_right, pop_right_i] = right.top();
                    right.pop();
                    while (!right.empty() && right.top().second <= i-x)
                        right.pop();
                    
                    left.push({pop_right, pop_right_i});
                    right.push({nums[i], i});

                    cost += 1LL * (l_size - r_size) * abs(right.top().first - mid);
                    mid = right.top().first;
                }
            } else {
                while (!right.empty() && right.top().second <= i-x)
                    right.pop();
                
                if (nums[i] >= left.top().first) {
                    right.push({nums[i], i});
                    if (mid < right.top().first)
                        cost += 1LL * (l_size - r_size) * abs(right.top().first - mid);
                    else
                        cost += 1LL * (r_size - l_size - 2) * abs(right.top().first - mid);
                    
                    mid = right.top().first;
                } else {
                    auto [pop_left, pop_left_i] = left.top();
                    left.pop();
                    while (!left.empty() && left.top().second <= i-x)
                        left.pop();
                    
                    left.push({nums[i], i});
                    right.push({pop_left, pop_left_i});
                    cost += 1LL * (r_size - l_size - 2) * abs(mid - pop_left);
                    mid = pop_left;
                }
            }

            costs.push_back(cost);
        }

        vector<long long> dp = {LLONG_MAX};
        for (int i = 0; i < n; ++i)
            dp.push_back(min(dp.back(), costs[i+1]));
        
        for (int i = 1; i < k; ++i) {
            vector<long long> new_dp(x, LLONG_MAX);
            for (int j = x; j <= n; ++j) {
                long long best = new_dp.back();
			    if (dp[j-x] != LLONG_MAX && costs[j] != LLONG_MAX)
				    best = min(best, dp[j-x]+costs[j]);

                new_dp.push_back(best);
            }
            
            dp = new_dp;
        }
        
        return dp.back();
    }
};
