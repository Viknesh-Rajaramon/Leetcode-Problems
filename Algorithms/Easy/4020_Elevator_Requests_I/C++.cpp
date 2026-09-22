class Solution {
public:
    int elevatorRequests(int n, vector<int>& requests) {
        int result = 0, curr = 0;
        for (int r : requests) {
            result += abs(r-curr);
            curr = r;
        }
        
        return result;
    }
};
