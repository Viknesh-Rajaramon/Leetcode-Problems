class Solution {
public:
    long long best_single(vector<long long>& prefix, int n, int l, int r) {
        deque<pair<int, long long>> queue;
        long long best = LLONG_MIN;
        for (int i = 1; i <= n; ++i) {
            int j = i-l;
            if (j >= 0) {
                while (!queue.empty() && queue.back().second >= prefix[j])
                    queue.pop_back();
                
                queue.push_back({j, prefix[j]});
            }

            while (!queue.empty() && queue[0].first < i-r)
                queue.pop_front();
            
            if (!queue.empty())
                best = max(best, prefix[i] - queue[0].second);
        }

        return best;
    }

    tuple<long long, int> check(long long cost, vector<long long>& prefix, int n, int l, int r) {
        vector<long long> dp_val(n+1);
        vector<int> dp_cnt(n+1);
        deque<tuple<int, long long, int>> queue;
        for (int i = 1; i <= n; ++i) {
            int j = i-l;
            if (j >= 0) {
                long long val = dp_val[j] - prefix[j];
                int cnt = dp_cnt[j];
                while (!queue.empty() && (get<1>(queue.back()) < val || (get<1>(queue.back()) == val && get<2>(queue.back()) >= cnt)))
                    queue.pop_back();
                
                queue.push_back({j, val, cnt});
            }

            while (!queue.empty() && get<0>(queue[0]) < i-r)
                queue.pop_front();
            
            dp_val[i] = dp_val[i-1];
            dp_cnt[i] = dp_cnt[i-1];
            if (!queue.empty()) {
                long long val = prefix[i] - cost + get<1>(queue[0]);
                int cnt = get<2>(queue[0]) + 1;
                if (val > dp_val[i] || (val == dp_val[i] && cnt < dp_cnt[i])) {
                    dp_val[i] = val;
                    dp_cnt[i] = cnt;
                }
            }
        }

        return {dp_val[n], dp_cnt[n]};
    }

    long long maximumSum(vector<int>& nums, int m, int l, int r) {
        int n = nums.size();
        vector<long long> prefix(n+1);
        for (int i = 0; i < n; ++i)
            prefix[i+1] = prefix[i] + nums[i];

        long long single = best_single(prefix, n, l, r), val = 0;
        int cnt = 0;
        tie(val, cnt) = check(0, prefix, n, l, r);
        if (cnt <= m)
            return cnt > 0 ? val : single;

        long long low = 0, high = 1;
        for (int num : nums)
            high += abs(num);

        while (low < high) {
            long long mid = (low+high) >> 1;
            tie(val, cnt) = check(mid, prefix, n, l, r);
            if (cnt > m)
                low = mid+1;
            else
                high = mid;
        }
        
        tie(val, cnt) = check(low, prefix, n, l, r);
        return max(single, val + low*m);
    }
};
