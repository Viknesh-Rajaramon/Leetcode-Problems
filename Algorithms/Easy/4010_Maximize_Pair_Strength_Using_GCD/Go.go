package main

func maxPairStrength(nums []int) int64 {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}

		return a
	}

	result, n := int64(0), len(nums)
	for i := range n {
		for j := i + 1; j < n; j++ {
			g := gcd(nums[i], nums[j])
			result = max(result, int64((nums[i]*nums[j])/(g*g)))
		}
	}

	return result
}
