class Solution {
public:
    vector<int> spf;
    void cal_spf() {
        for (int i = 0; i <= 1e5; ++i)
            spf[i] = i;
        
        for (int i = 2; i <= 1e5; ++i) {
            if (spf[i] != i)
                continue;
            
            for (long long j=1LL*i*i; j <= 1e5; j += i)
                if (spf[j] == j)
                    spf[j] = i;
        }
    }

    int maxScore(vector<int>& nums, int maxVal) {
        int n = nums.size();
        spf.assign(1e5+1, 0);
        cal_spf();
        int maxi = *max_element(nums.begin(), nums.end());
        vector <int> mpp(100001, 0);
        for (int i = 0; i < n; ++i)
            mpp[nums[i]]++;
        
        vector<int> div(1e5+1, 0);
        div[1] = n;
        for (int i = 2; i <= 1e5; ++i)
            for (int j = i; j <= 1e5; j += i)
                div[i] += mpp[j];
        
        int result = -1e9;
        for(int x = 1; x <= max(maxVal, maxi); ++x) {
            if(mpp[x] == 0 && x > maxVal)
                continue;
            
            int temp = x;
            vector<int> vec;
            while(temp > 1) {
                int p = spf[temp];
                vec.push_back(p);
                while(temp % p == 0)
                    temp /= p;
            }

            int siz = vec.size(), total = 0;
            int subsets = (1 << siz);
            for(int i = 1; i < subsets; ++i) {
                int mul = 1, num = 0;
                for(int j = 0; j < siz; ++j) {
                    if ((i & (1 << j)) != 0) {
                        mul *= vec[j];
                        ++num;
                    }
                }

                if (num%2 == 0)
                    total -= div[mul];
                else
                    total += div[mul];
            }

            int cost = (mpp[x] == 0) ? max(1, total) : ((x == 1) ? 0 : total-1);
            result = max(result, x-cost);
        }

        return result;
    }
};
