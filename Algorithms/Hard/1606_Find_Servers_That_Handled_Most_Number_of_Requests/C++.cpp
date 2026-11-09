class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        priority_queue<tuple<int, int>, vector<tuple<int, int>>, greater<>> busy;
        priority_queue<int, vector<int>, greater<>> available;
        vector<int> num_processed(k);
        for (int i = 0; i < k; ++i)
            available.push(i);
        
        for (int i = 0; i < arrival.size(); ++i) {
            while (!busy.empty()) {
                if (get<0>(busy.top()) <= arrival[i]) {
                    auto [_, server] = busy.top();
                    busy.pop();
                    available.push(i + (k + ((server-i) % k)) % k);
                } else {
                    break;
                }
            }

            if (available.empty())
                continue;
            
            int virtual_server = available.top();
            available.pop();
            int next_server = virtual_server % k;
            ++num_processed[next_server];
            busy.push({arrival[i] + load[i], next_server});
        }
        
        vector<int> result;
        int max_reqs = *max_element(num_processed.begin(), num_processed.end());
        for (int i = 0; i < k; ++i)
            if (num_processed[i] == max_reqs)
                result.push_back(i);
        
        return result;
    }
};
