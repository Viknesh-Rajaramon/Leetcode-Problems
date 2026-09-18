package main

func maximumWidth(planks []int) int {
	freq, height, values := make(map[int]int), make(map[int]int), make([]int, 0)
	for _, plank := range planks {
		if _, exists := freq[plank]; !exists {
			freq[plank] = 0
		}

		freq[plank]++
	}

	for key := range freq {
		height[key] = freq[key]
		values = append(values, key)
	}

	n := len(values)
	for i := range n {
		a := values[i]
		for j := i; j < n; j++ {
			b := values[j]
			h := a + b
			if _, exists := height[h]; !exists {
				height[h] = 0
			}

			count := freq[a] / 2
			if a != b {
				count = min(freq[a], freq[b])
			}

			height[h] += count
		}
	}

	result := 0
	for h := range height {
		result = max(result, height[h])
	}

	return result
}
