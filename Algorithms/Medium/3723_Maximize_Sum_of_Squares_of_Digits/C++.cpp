class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        if (sum > 9*num)
		    return "";

        string result(sum/9, '9');
        int r = sum%9;
        if (r > 0)
            result.push_back('0' + r);

        result.append(num - (int)result.size(), '0');
        return result;
    }
};
