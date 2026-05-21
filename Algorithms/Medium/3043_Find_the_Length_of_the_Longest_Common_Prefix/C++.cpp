#include <vector>
#include <string>

class Solution {
public:
    int digits(int num) {
        int count = 0;
        while (num > 0) {
            ++count;
            num /= 10;
        }

        return count;
    }

    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        unordered_set<int> prefixes;
        for (int num : arr1) {
            int x = num;
            while (x > 0) {
                prefixes.insert(x);
                x /= 10;
            }
        }

        int result = 0;
        for (int num : arr2) {
            int x = num, len = digits(num);
            while (x > 0) {
                if (prefixes.count(x)) {
                    result = max(result, len);
                    break;
                }
                
                x /= 10;
                --len;
            }
        }

        return result;
    }
};
