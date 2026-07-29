package main

func smallestPalindrome(s string) string {
	result, n, counter := make([]byte, 0), len(s), make([]int, 26)
	for i := 0; i < n/2; i++ {
		counter[s[i]-'a']++
	}

	for i := 0; i < 26; i++ {
		c := byte('a' + i)
		for j := 0; j < counter[i]; j++ {
			result = append(result, c)
		}
	}

	if n%2 == 1 {
		result = append(result, s[n/2])
	}

	for i := 25; i >= 0; i-- {
		c := byte('a' + i)
		for j := 0; j < counter[i]; j++ {
			result = append(result, c)
		}
	}

	return string(result)
}
