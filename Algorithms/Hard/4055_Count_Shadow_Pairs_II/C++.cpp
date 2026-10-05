class Solution {
public:
    int shadowPairs(vector<int>& nums) {
        vector<int> values = nums;
        sort(values.begin(), values.end());
        values.erase(unique(values.begin(), values.end()), values.end());
        int n = values.size();
        if (n == 1)
            return 0;
        
        unordered_map<int, int> ranks;
        ranks.reserve(n<<1);
        for (int i = 0; i < n; ++i)
            ranks[values[i]] = i;
        
        vector<int> initial;
        initial.reserve(nums.size());
        for (int value : nums) {
            initial.push_back(ranks[value]);
        }

        struct Task {
            vector<int> sequence;
            int low;
            int high;
        };

        vector<Task> tasks;
        tasks.push_back({move(initial), 0, n-1});

        int result = 0;
        while (!tasks.empty()) {
            Task task = move(tasks.back());
            tasks.pop_back();

            vector<int>& sequence = task.sequence;
            int low = task.low, high = task.high;
            int mid = (low + high) >> 1;
            vector<int> left, right, stack, caps, starts;
            left.reserve(sequence.size());
            right.reserve(sequence.size());
            stack.reserve(sequence.size());
            caps.reserve(sequence.size());
            starts.reserve(sequence.size());
            for (int x : sequence) {
                if (x <= mid) {
                    left.push_back(x);
                    while (!stack.empty() && stack.back() < x)
                        stack.pop_back();

                    int size = stack.size();
                    while (!starts.empty() && starts.back() >= size) {
                        starts.pop_back();
                        caps.pop_back();
                    }

                    stack.push_back(x);
                    if (caps.empty() || caps.back() != n) {
                        caps.push_back(n);
                        starts.push_back(size);
                    }
                } else {
                    right.push_back(x);
                    if (!caps.empty() && caps.back() >= x) {
                        int start = starts.back();
                        starts.pop_back();
                        caps.pop_back();
                        while (!caps.empty() && caps.back() >= x) {
                            start = starts.back();
                            starts.pop_back();
                            caps.pop_back();
                        }

                        result += (int)stack.size() - start;
                        caps.push_back(x);
                        starts.push_back(start);
                    }
                }
            }

            if (low < mid && left.size() > 1)
                tasks.push_back({move(left), low, mid});
            
            if (mid+1 < high && right.size() > 1)
                tasks.push_back({move(right), mid+1, high});
        }

        return result;
    }
};
