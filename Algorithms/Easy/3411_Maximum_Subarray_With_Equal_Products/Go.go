package main

func maxLength(nums []int) int {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}

		return a
	}

	result, prod, l := 2, 1, 0
	for r := range len(nums) {
		for gcd(prod, nums[r]) > 1 {
			prod /= nums[l]
			l++
		}

		prod *= nums[r]
		result = max(result, r-l+1)
	}

	return result
}
