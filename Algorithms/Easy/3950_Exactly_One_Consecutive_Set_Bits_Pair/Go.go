func consecutiveSetBits(n int) bool {
	n = n & (n >> 1)
	return (n > 0) && !((n & (n - 1)) != 0)
}
