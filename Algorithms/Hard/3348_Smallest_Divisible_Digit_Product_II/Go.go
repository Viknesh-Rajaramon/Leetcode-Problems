package main

import (
	"strings"
)

func smallestNumber(num string, t int64) string {
	gcd := func(a, b int64) int64 {
		for b != 0 {
			a, b = b, a%b
		}

		return a
	}

	check := func(a, b string) bool {
		if len(a) > len(b) {
			return true
		}

		if len(a) < len(b) {
			return false
		}

		return a > b
	}

	n := len(num)
	remind, end := make([]int64, n+1), n
	remind[0] = t

	for i := 0; i < n; i++ {
		if num[i] == '0' {
			end = i + 1
			break
		}

		remind[i+1] = remind[i] / gcd(remind[i], int64(num[i]-'0'))
	}

	if end == n && remind[n] == 1 {
		return num
	}

	numBytes := []byte(num)
	for i := end - 1; i >= 0; i-- {
		for numBytes[i] < '9' {
			tt := remind[i]
			numBytes[i]++
			tt /= gcd(tt, int64(numBytes[i]-'0'))
			for j := n - 1; j > i; j-- {
				for k := 9; k > 0; k-- {
					if tt%int64(k) == 0 {
						tt /= int64(k)
						numBytes[j] = byte('0' + k)
						break
					}
				}
			}

			if tt == 1 {
				return string(numBytes)
			}
		}
	}

	var res strings.Builder
	for i := 9; t > 1 && i > 1; i-- {
		for t%int64(i) == 0 {
			res.WriteByte(byte('0' + i))
			t /= int64(i)
		}
	}

	if t != 1 {
		return "-1"
	}

	resStr := []byte(res.String())
	for i, j := 0, len(resStr)-1; i < j; i, j = i+1, j-1 {
		resStr[i], resStr[j] = resStr[j], resStr[i]
	}

	result := string(resStr)
	if check(result, num) {
		return result
	}

	if len(result) == len(num) {
		return "1" + result
	}

	dif := len(num) - len(result)
	ones := strings.Repeat("1", dif)
	if check(ones+result, num) {
		return ones + result
	}

	return strings.Repeat("1", dif+1) + result
}
