package main

func maximumMEX(nums []int) []int {
	n, mx, mex, curr_mex := len(nums), 100_002, 0, 0
	total_cnt, curr_cnt := make([]int, mx), make([]int, mx)
	for _, num := range nums {
		total_cnt[num]++
	}

	for total_cnt[mex] > 0 {
		mex += 1
	}

	result, l := make([]int, 0), 0
	for r := 0; r < n; r++ {
		curr_cnt[nums[r]]++
		for curr_cnt[curr_mex] > 0 {
			curr_mex++
		}

		if curr_mex == mex {
			result = append(result, mex)
			for i := l; i <= r; i++ {
				total_cnt[nums[i]]--
				curr_cnt[nums[i]]--
				if total_cnt[nums[i]] == 0 {
					mex = min(mex, nums[i])
				}
			}

			curr_mex = 0
			l = r + 1
		}
	}

	return result
}
