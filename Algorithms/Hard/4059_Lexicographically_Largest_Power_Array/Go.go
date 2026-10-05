package main

func largestPower(nums []int) []int {
	result, old_temp := make([]int, 0), make([][]int, 0)
	old_temp = append(old_temp, nums)
	for bit := 14; bit >= 0; bit-- {
		mask, count, splitting, new_temp := 1<<bit, 0, true, make([][]int, 0)
		for _, section := range old_temp {
			if splitting {
				section_0, section_1 := make([]int, 0), make([]int, 0)
				for _, num := range section {
					if num&mask != 0 {
						section_1 = append(section_1, num)
					} else {
						section_0 = append(section_0, num)
					}
				}

				if len(section_1) > 0 {
					count += len(section_1)
					new_temp = append(new_temp, section_1)
				}

				if len(section_0) > 0 {
					splitting = false
					new_temp = append(new_temp, section_0)
				}
			} else {
				new_temp = append(new_temp, section)
			}
		}

		result = append(result, count)
		old_temp = new_temp
	}

	return result
}
