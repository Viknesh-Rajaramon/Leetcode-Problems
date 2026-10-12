package main

func maxSum(nums []int, k int) int {
	mod, count := int(1e9+7), make([]int, 30)
	for _, num := range nums {
		for i := range 30 {
			if num&(1<<i) != 0 {
				count[i]++
			}
		}
	}

	result := 0
	for range k {
		curr := 0
		for j := 29; j >= 0; j-- {
			if count[j] == 0 {
				continue
			}

			curr |= 1 << j
			count[j]--
		}

		result = (result + curr*curr) % mod
	}

	return result
}
