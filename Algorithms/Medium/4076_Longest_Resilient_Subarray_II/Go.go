package main

func resilientSubarray(nums []int, k int) int {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}

		return a
	}

	result, n, i := 1, len(nums), 0
	for i < n {
		r, j := nums[i]%k, i
		for j < n && nums[j]%k == r {
			j++
		}

		g := k / gcd(r, k)
		result = max(result, 1+((j-i-1)/g)*g)
		i = j
	}

	return result
}
