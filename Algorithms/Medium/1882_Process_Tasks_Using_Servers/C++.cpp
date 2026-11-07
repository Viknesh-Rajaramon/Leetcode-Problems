class Solution {
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        vector<int> result;
        priority_queue<tuple<long long, int, int>, vector<tuple<long long, int, int>>, greater<>> busy;
        priority_queue<tuple<int, int, long long>, vector<tuple<int, int, long long>>, greater<>> idle;
        for (int i = 0; i < servers.size(); ++i)
            idle.push({servers[i], i, 0});

        for (int i = 0; i < tasks.size(); ++i) {
            while (!busy.empty() && get<0>(busy.top()) <= i) {
                auto [t, w, idx] = busy.top();
                busy.pop();
                idle.push({w, idx, t});
            }

            if (!idle.empty()) {
                auto [w, idx, t] = idle.top();
                idle.pop();
                result.push_back(idx);
                busy.push({i + tasks[i], w, idx});
            } else {
                auto [t, w, idx] = busy.top();
                busy.pop();
                result.push_back(idx);
                busy.push({t + tasks[i], w, idx});
            }
        }

        return result;
    }
};
