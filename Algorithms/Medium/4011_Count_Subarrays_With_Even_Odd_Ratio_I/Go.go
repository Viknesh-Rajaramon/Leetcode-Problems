package main

func countRatioSubarrays(nums []int, a int, b int) int {
	result, n := 0, len(nums)
	for i := range n {
		x, y := 0, 0
		for j := i; j < n; j++ {
			if nums[j]%2 == 0 {
				x++
			} else {
				y++
			}

			if y > 0 && x*b <= a*y {
				result++
			}
		}
	}

	return result
}
