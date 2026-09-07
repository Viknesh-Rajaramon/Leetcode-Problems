package main

func distinctSubseqII(s string) int {
	dp, last := 1, make([]int, 26)
	const mod = 1e9 + 7
	for _, c := range s {
		new_dp := (dp*2 - last[c-'a'] + mod) % mod
		last[c-'a'], dp = dp, new_dp
	}

	return (dp - 1 + mod) % mod
}
