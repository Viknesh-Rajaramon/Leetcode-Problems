package main

func distantSubarrays(nums []int, goal int, k int) int64 {
	n := len(nums)
	result := int64(n * (n + 1) / 2)
	if k == 0 {
		return result
	}

	a, temp, prefix, k1, k2 := make([]int64, n+1), make([]int64, n+1), int64(0), int64(goal-k+1), int64(goal+k-1)
	for i, num := range nums {
		prefix += int64(num)
		a[i+1] = prefix
	}

	var ff func(low, high int)
	ff = func(low, high int) {
		if low >= high {
			return
		}

		mid := (low + high) >> 1
		ff(low, mid)
		ff(mid+1, high)
		p1, p2 := mid+1, mid+1
		for i := low; i <= mid; i++ {
			for p1 <= high && a[p1] < a[i]+k1 {
				p1++
			}

			for p2 <= high && a[p2] <= a[i]+k2 {
				p2++
			}

			result -= int64(p2 - p1)
		}

		i, j, p := low, mid+1, low
		for i <= mid && j <= high {
			if a[i] <= a[j] {
				temp[p] = a[i]
				i++
			} else {
				temp[p] = a[j]
				j++
			}

			p++
		}

		for i <= mid {
			temp[p] = a[i]
			i++
			p++
		}

		for j <= high {
			temp[p] = a[j]
			j++
			p++
		}

		for p = low; p <= high; p++ {
			a[p] = temp[p]
		}
	}

	ff(0, n)
	return result
}
