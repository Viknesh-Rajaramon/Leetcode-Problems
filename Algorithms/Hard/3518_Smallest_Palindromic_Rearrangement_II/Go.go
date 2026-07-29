package main

func smallestPalindrome(s string, k int) string {
	n, count := len(s), make([]int, 26)
	for i := 0; i < n/2; i++ {
		count[s[i]-'a']++
	}

	total, counting, remain, i := 0, 1, 0, 0
	for i = 25; i >= 0; i-- {
		for c := 1; c <= count[i]; c++ {
			total++
			counting = counting * total / c
			if counting >= k {
				remain = count[i] - c
				break
			}
		}

		if counting >= k {
			break
		}
	}

	if counting < k {
		return ""
	}

	result, l := make([]byte, n), 0
	for j := 0; j <= i; j++ {
		x, c := byte('a'+j), count[j]
		if j == i {
			c = remain
		}

		for p := 0; p < c; p++ {
			count[j]--
			result[l] = x
			l++
		}
	}

	for total > 0 {
		for j := i; j < 26; j++ {
			if count[j] == 0 {
				continue
			}

			new_count := int64(counting) * int64(count[j]) / int64(total)
			if new_count < int64(k) {
				k -= int(new_count)
				continue
			}

			counting = int(new_count)
			count[j]--
			total--
			result[l] = byte('a' + j)
			l++
			break
		}
	}

	if n&1 == 1 {
		result[l] = s[n/2]
		l++
	}

	for i := l - 1 - n%2; i >= 0; i-- {
		result[l] = result[i]
		l++
	}

	return string(result[:l])
}
