class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        long long result = LLONG_MIN, p_0 = LLONG_MIN, m_0 = LLONG_MIN, p_1 = LLONG_MIN, m_1 = LLONG_MIN;
        for (int num : nums) {
            long long np_0 = num, nm_0 = LLONG_MIN, np_1 = p_0, nm_1 = m_0;
            if (m_0 != LLONG_MIN)
                np_0 = max(np_0, m_0+num);

            if (p_0 != LLONG_MIN)
                nm_0 = p_0 - num;

            if (m_1 != LLONG_MIN)
                np_1 = max(np_1, m_1+num);

            if (p_1 != LLONG_MIN)
                nm_1 = max(nm_1, p_1-num);

            p_0 = np_0;
            p_1 = np_1;
            m_0 = nm_0;
            m_1 = nm_1;
            result = max({result, p_1, m_1, m_0, p_0});
        }

        return result;
    }
};
