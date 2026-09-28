package main

func largestString(nums []int) []string {
	result := make([]string, 0)
	for _, num := range nums {
		curr, z := make([]byte, 0), num/(1<<25)
		if z > 0 {
			num %= (1 << 25)
			for i := 0; i < z; i++ {
				curr = append(curr, 'z')
			}
		}

		for i := 24; i >= 0; i-- {
			if num&(1<<i) != 0 {
				curr = append(curr, byte('a'+i))
			}
		}

		result = append(result, string(curr))
	}

	return result
}
