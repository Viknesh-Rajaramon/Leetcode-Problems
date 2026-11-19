class Solution {
public:
    int minimizeSum(vector<int>& nums) {
        vector<int> max_heap(3, INT_MIN), min_heap(3, INT_MAX);
        for (int num : nums) {
            if (num < min_heap[0]) {
                min_heap[2] = min_heap[1];
                min_heap[1] = min_heap[0];
                min_heap[0] = num;
            } else if (num < min_heap[1]) {
                min_heap[2] = min_heap[1];
                min_heap[1] = num;
            } else if (num < min_heap[2]) {
                min_heap[2] = num;
            }

            if (num > max_heap[0]) {
                max_heap[2] = max_heap[1];
                max_heap[1] = max_heap[0];
                max_heap[0] = num;
            } else if (num > max_heap[1]) {
                max_heap[2] = max_heap[1];
                max_heap[1] = num;
            } else if (num > max_heap[2]) {
                max_heap[2] = num;
            }
        }
        
        return min({max_heap[2]-min_heap[0], max_heap[1]-min_heap[1], max_heap[0]-min_heap[2]});
    }
};
