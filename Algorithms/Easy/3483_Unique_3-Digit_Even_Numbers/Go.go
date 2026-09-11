package main

func totalNumbers(digits []int) int {
	freq := make([]int, 10)
	for _, d := range digits {
		freq[d]++
	}

	result := 0
	for i := 1; i < 10; i++ {
		if freq[i] == 0 {
			continue
		}

		freq[i]--
		for j := range 10 {
			if freq[j] == 0 {
				continue
			}

			freq[j]--
			for k := 0; k < 10; k += 2 {
				if freq[k] == 0 {
					continue
				}

				result++
			}

			freq[j]++
		}

		freq[i]++
	}

	return result
}
