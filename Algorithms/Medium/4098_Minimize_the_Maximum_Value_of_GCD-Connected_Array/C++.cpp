class Solution {
public:
    long long minimumMaxValue(int n, int index, int value) {
        function<int(int)> get_spf = [&](int x) {
            if (x < 2)
                return 0;
            
            if (x%2 == 0)
                return 2;
            
            if (x%3 == 0)
                return 3;
            
            int i = 5;
            while (i*i <= x) {
                if (x%i == 0)
                    return i;
                
                if (x%(i+2) == 0)
                    return i+2;
                
                i += 6;
            }
            
            return x;
        };

        if (value == 1)
            return -1;

        if (index > 0) {
            int min_left = 0;
            if (value % 2 == 0) {
                min_left = value - 2*index;
            } else {
                int spf = get_spf(value);
                if (spf == 0)
                    return -1;
                
                min_left = value - spf - 2*(index-1);
            }
            
            if (min_left <= 0)
                return -1;
        }

        if (index == n-1)
            return value;
            
        if (value%2 == 0)
            return 2LL*(n-1-index) + value;
            
        int spf = get_spf(value);
        if (spf == 0)
            return -1;
        
        return 2LL*(n-2-index) + value + spf;
    }
};
