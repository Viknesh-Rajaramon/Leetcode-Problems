class Solution {
public:
    int maxDistance(string moves) {
        int x = 0, y = 0, extra = 0;
        for (char c : moves) {
            if (c == 'R')
			    ++x;
		    else if (c == 'L')
			    --x;
		    else if (c == 'U')
			    ++y;
		    else if (c == 'D')
			    --y;
		    else
			    ++extra;
        }

        return abs(x) + abs(y) + extra;
    }
};
