package main

func countSpecialIntegers(nums []int) int {
	first, last, freq := make(map[int]int), make(map[int]int), make(map[int]int)
	for i, num := range nums {
		if _, ok := first[num]; !ok {
			first[num] = i
			freq[num] = 0
		}

		last[num] = i
		freq[num]++
	}

	result := 0
	for num := range freq {
		if last[num]-first[num]+1 == freq[num] {
			result++
		}
	}

	return result
}
