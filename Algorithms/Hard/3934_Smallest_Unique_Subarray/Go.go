package main

func smallestUniqueSubarray(nums []int) int {
	const MOD int64 = 1000000007
	const BASE int64 = 911382323

	n := len(nums)
	hash := make([]int64, n+1)
	powers := make([]int64, n+1)
	powers[0] = 1

	for i, num := range nums {
		hash[i+1] = (hash[i]*BASE + int64(num)) % MOD
		powers[i+1] = powers[i] * BASE % MOD
	}

	check := func(length int) bool {
		counts := make(map[int64]int, n-length+1)
		for l := 0; l+length <= n; l++ {
			key := (hash[l+length] - hash[l]*powers[length]%MOD + MOD) % MOD
			counts[key]++
		}

		for _, times := range counts {
			if times == 1 {
				return true
			}
		}

		return false
	}

	low, high := 1, n
	for low < high {
		mid := (low + high) >> 1
		if check(mid) {
			high = mid
		} else {
			low = mid + 1
		}
	}

	return low
}
