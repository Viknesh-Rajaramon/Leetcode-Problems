class Solution {
public:
    bool canAliceWin(int n) {
        bool result = false;
        int take = 10;
        while (n >= take) {
            n -= take--;
            result = !result;
        }
        
        return result;
    }
};
