#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        int n = A.size(), count = 0;
        vector<int> result(n), freq(n+1, 0);
        for (int i = 0; i < n; ++i) {
            freq[A[i]]++;
            if (freq[A[i]] == 2)
                ++count;

            freq[B[i]]++;
            if (freq[B[i]] == 2)
                ++count;

            result[i] = count;
        }

        return result;
    }
};
