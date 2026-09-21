class Solution {
public:
    double minPrice(vector<int>& prices, vector<int>& discounts) {
        sort(prices.rbegin(), prices.rend());
        sort(discounts.rbegin(), discounts.rend());

        long long result = 0;
        for (int i = 0; i < prices.size(); ++i) {
            if (i < discounts.size())
                result += prices[i] * (100 - discounts[i]);
            else
                result += prices[i] * 100;
        }

        return double(result) / 100;
    }
};
