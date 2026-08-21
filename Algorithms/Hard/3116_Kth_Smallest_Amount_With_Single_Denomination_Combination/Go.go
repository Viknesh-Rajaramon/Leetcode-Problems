package main

import (
	"math/bits"
	"sort"
)

func findKthSmallest(coins []int, k int) int64 {
	sort.Ints(coins)
	new_coins := make([]int, 0)
	for i := range coins {
		is_valid := true
		for j := 0; j < i; j++ {
			if coins[i]%coins[j] == 0 {
				is_valid = false
				break
			}
		}

		if is_valid {
			new_coins = append(new_coins, coins[i])
		}
	}

	n := 1 << len(new_coins)
	lcm, left, right := make([]int64, n), int64(k), int64(new_coins[0]*k+1)
	lcm[0] = 1
	for mask := 1; mask < n; mask++ {
		pre_mask := mask & (mask - 1)
		i := bits.TrailingZeros(uint(mask))
		tmp := lcm[pre_mask] / gcd(lcm[pre_mask], int64(new_coins[i]))
		if tmp <= right/int64(new_coins[i]) {
			lcm[mask] = tmp * int64(new_coins[i])
		} else {
			lcm[mask] = right + 1
		}
	}

	get := func(x int64) int64 {
		count := int64(0)
		for mask := 1; mask < n; mask++ {
			if lcm[mask] > x {
				continue
			}

			if bits.OnesCount(uint(mask))&1 == 1 {
				count += x / lcm[mask]
			} else {
				count -= x / lcm[mask]
			}
		}

		return count
	}

	for left < right {
		mid := (left + right) >> 1
		if get(mid) >= int64(k) {
			right = mid
		} else {
			left = mid + 1
		}
	}

	return left
}

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
