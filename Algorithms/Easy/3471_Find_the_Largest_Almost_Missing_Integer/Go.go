package main

func largestInteger(nums []int, k int) int {
	n, hash_map := len(nums), make(map[int]int)
	for i := 0; i <= n-k; i++ {
		s := make(map[int]bool)
		for j := i; j < i+k; j++ {
			if !s[nums[j]] {
				s[nums[j]] = true
			}
		}

		for num, _ := range s {
			hash_map[num] += 1
		}
	}

	result := -1
	for key, val := range hash_map {
		if val == 1 {
			result = max(result, key)
		}
	}

	return result
}
