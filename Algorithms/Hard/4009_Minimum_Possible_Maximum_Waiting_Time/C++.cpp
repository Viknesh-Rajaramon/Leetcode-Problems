class Solution {
public:
    int minMaxWaitingTime(vector<int>& demand, vector<int>& fuel) {
        int n = demand.size();
        function<int(int)> check = [&](int wait_limit) {
            set<tuple<int, int, int, int>> states;
            int served = 0;
            states.insert({fuel[0], fuel[1], 0, 0});
            for (int i = 0; i < n; ++i) {
                set<tuple<int, int, int, int>> nxt;
                for (auto& [f0, f1, t0, t1] : states) {
                    if (f0 >= demand[i] && t0 <= wait_limit)
                        nxt.insert({f0 - demand[i], f1, demand[i], max(0, t1 - t0)});

                    if (f1 >= demand[i] && t1 <= wait_limit)
                        nxt.insert({f0, f1 - demand[i], max(0, t0 - t1), demand[i]});
                }
                
                if (nxt.size() == 0)
                    break;

                states = nxt;
                ++served;
            }
            
            return served;
        };
        
        int mx = check(1e9);
        if (mx == 0)
            return -1;

        int low = 0, high = 0;
        for (int num : demand)
            high += num;

        while (low <= high) {
            int mid = (low + high) >> 1;
            if (check(mid) == mx)
                high = mid - 1;
            else
                low = mid + 1;
        }

        return low;
    }
};
