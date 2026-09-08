package main

func getLength(nums []int) int {
	result, n := 1, len(nums)
	for l := 0; l < n; l++ {
		count, freq, min_, max_, distinct, occupied := make(map[int]int), make([]int, n+1), n+1, 0, 0, 0
		for r := l; r < n; r++ {
			old := count[nums[r]]
			new := old + 1
			count[nums[r]] = new
			if old == 0 {
				distinct++
				min_ = 1
			} else {
				freq[old]--
				if freq[old] == 0 {
					occupied--
				}
			}

			if freq[new] == 0 {
				occupied++
			}

			freq[new]++
			max_ = max(max_, new)

			if old > 0 && old == min_ && freq[old] == 0 {
				for freq[min_] == 0 {
					min_++
				}
			}

			if distinct == 1 || (occupied == 2 && max_ == 2*min_) {
				result = max(result, r-l+1)
			}
		}
	}

	return result
}
