class Solution {
public:
    int minLights(vector<int>& lights) {
        int n = lights.size();
	    vector<int> diff(n+1);
	    for (int i = 0; i < n; ++i) {
		    if (lights[i] == 0)
			    continue;

		    ++diff[max(0, i-lights[i])];
		    --diff[min(n-1, i+lights[i])+1];
	    }

	    for (int i = 0; i < n; ++i)
		    diff[i+1] += diff[i];

	    int result = 0, length = 0;
        for (int i = 0; i < n; ++i) {
            if (diff[i] == 0) {
                ++length;
            } else {
                result += (length + 2) / 3;
                length = 0;
            }
        }

        result += (length + 2) / 3;
        return result;
    }
};
