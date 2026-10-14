package main

func maxSumOfSquares(num int, sum int) string {
	if sum > 9*num {
		return ""
	}

	result, r := make([]byte, 0, num), sum%9
	for range sum / 9 {
		result = append(result, '9')
	}

	if r > 0 {
		result = append(result, byte('0'+r))
	}

	zeros := num - len(result)
	for range zeros {
		result = append(result, '0')
	}

	return string(result)
}
