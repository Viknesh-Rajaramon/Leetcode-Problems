package main

func canMakeSubsequence(s string, t string) bool {
	m, n := len(s), len(t)
	if m > n {
		return false
	}

	var rch byte
	replaced, i, j := false, 0, 0
	for i < m && j < n {
		if s[i] == t[j] {
			i++
		} else {
			if !replaced {
				replaced, rch = true, s[i]
				i++
			} else {
				if rch == t[j] {
					replaced = false
				}
			}
		}

		j++
	}

	return i == m
}
