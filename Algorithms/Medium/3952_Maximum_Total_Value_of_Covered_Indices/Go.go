func maxTotal(nums []int, s string) int64 {
	var prev int64 = 0
	var curr int64 = 0
	if s[0] == '1' {
		curr = int64(nums[0])
	}

	for i := 1; i < len(nums); i++ {
		if s[i] == '1' {
			prev += int64(nums[i-1])
			curr = max(curr+int64(nums[i]), prev)
		} else {
			prev = curr
		}
	}

	return curr
}
