class Fenwick {
private:
    int n;
    vector<int> bit;

public:
    Fenwick(int n) : n(n), bit(n+1, 0) {}

    void add(int i, int delta) {
        ++i;
        while (i <= n) {
            bit[i] += delta;
            i += i & -i;
        }
    }

    int sum(int i) {
        if (i < 0)
            return 0;

        ++i;
        int res = 0;
        while (i > 0) {
            res += bit[i];
            i -= i & -i;
        }

        return res;
    }

    int range_sum(int l, int r) {
        return r >= l ? sum(r) - sum(l-1) : 0;
    }
};

class Solution {
public:
    vector<long long> countOfPeaks(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        function<bool(int)> is_peak = [&](int i) {
            return 0 < i && i < n-1 && nums[i] > nums[i-1] && nums[i] > nums[i+1];
        };

        function<int(int)> f_len = [&](int L) {
            return L >= 3 ? (L - 2) * (L - 1) / 2 : 0;
        };

        Fenwick bit(n);
        vector<int> peaks;
        unordered_map<int, int> gap_val;
        for (int i = 1; i < n-1; ++i) {
            if (is_peak(i)) {
                peaks.push_back(i);
            }
        }

        function<int(int, int)> compute_gap_val = [&](int left_peak, int right_peak) {
            return (right_peak != 0) ? f_len(right_peak - left_peak + 1) : 0;
        };

        for (int i = 0; i < (int)peaks.size()-1; ++i) {
            int val = compute_gap_val(peaks[i], peaks[i+1]);
            gap_val[peaks[i]] = val;
            if (val != 0)
                bit.add(peaks[i], val);
        }

        if (!peaks.empty()) {
            gap_val[peaks.back()] = 0;
        }

        function<void(int)> add_peak = [&](int p) {
            if (gap_val.find(p) != gap_val.end())
                return;

            int i = distance(peaks.begin(), lower_bound(peaks.begin(), peaks.end(), p));
            int left = (i-1 >= 0)? peaks[i-1] : -1;
            int right = (i < (int)peaks.size()) ? peaks[i] : -1;
            peaks.insert(peaks.begin()+i, p);
            if (left != -1) {
                int new_val = compute_gap_val(left, p);
                int prev = gap_val.count(left) ? gap_val[left] : 0;
                if (new_val != prev) {
                    bit.add(left, new_val - prev);
                    gap_val[left] = new_val;
                }
            }

            int new_val_p = compute_gap_val(p, right);
            gap_val[p] = new_val_p;
            if (new_val_p)
                bit.add(p, new_val_p);
        };

        function<void(int)> remove_peak = [&](int p) {
            if (gap_val.find(p) == gap_val.end())
                return;
            
            int i = distance(peaks.begin(), lower_bound(peaks.begin(), peaks.end(), p));
            int left = (i-1 >= 0)? peaks[i-1] : -1;
            int right = (i+1 < peaks.size()) ? peaks[i+1] : -1;
            int prev_p = gap_val.count(p) ? gap_val[p] : 0;
            if (prev_p)
                bit.add(p, -prev_p);

            gap_val.erase(p);
            peaks.erase(peaks.begin() + i);
            if (left != -1) {
                int new_val = compute_gap_val(left, right);
                int prev = gap_val.count(left) ? gap_val[left] : 0;
                if (new_val != prev) {
                    bit.add(left, new_val - prev);
                    gap_val[left] = new_val;
                }
            }
        };

        function<long long(int)> total_subarrays_len_ge_3 = [&](int L) {
            return (L >= 3) ? (1LL * L * (L + 1) / 2 - (2 * L - 1)) : 0;
        };

        vector<long long> result;
        for (auto& q : queries) {
            if (q[0] == 1) {
                long long total = total_subarrays_len_ge_3(q[2] - q[1] + 1);
                if (total == 0) {
                    result.push_back(0);
                    continue;
                }

                int Lidx = distance(peaks.begin(), lower_bound(peaks.begin(), peaks.end(), q[1] + 1));
                int Ridx = distance(peaks.begin(), upper_bound(peaks.begin(), peaks.end(), q[2] - 1)) - 1;
                if (Lidx > Ridx) {
                    result.push_back(0);
                    continue;
                }

                int internal_sum = (Lidx <= Ridx-1) ? bit.range_sum(peaks[Lidx], peaks[Ridx-1]) : 0;
                int no_peak_subarrays = f_len(peaks[Lidx]-q[1]+1) + internal_sum + f_len(q[2]-peaks[Ridx]+1);
                result.push_back(total - no_peak_subarrays);
            }
            else {
                if (nums[q[1]] == q[2])
                    continue;

                nums[q[1]] = q[2];
                for (int j : {q[1] - 1, q[1], q[1] + 1}) {
                    if (j <= 0 || j >= n-1)
                        continue;

                    bool now = is_peak(j);
                    bool was = gap_val.find(j) != gap_val.end();
                    if (now && !was) {
                        add_peak(j);
                    } else if (!now && was) {
                        remove_peak(j);
                    }
                }
            }
        }

        return result;
    }
};
