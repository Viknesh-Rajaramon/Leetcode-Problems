class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        if (ranges::count(s, '1') < k)
            return "";
        
        string result = s;
        int count = 0;
        for (int left = 0, right = 0; right < s.length(); ++right) {
            count += s[right] - '0';
            while (count > k || s[left] == '0')
                count -= s[left++] - '0';
            
            if (count < k)
                continue;
            
            string t = s.substr(left, right+1-left);
            if (t.length() < result.length() || t.length() == result.length() && t < result)
                result = move(t);
        }

        return result;
    }
};
