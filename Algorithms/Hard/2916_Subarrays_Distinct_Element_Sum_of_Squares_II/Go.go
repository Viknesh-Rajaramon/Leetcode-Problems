package main

type BIT struct {
	size           int
	tree_1, tree_2 map[int]int
}

func NewBIT(n int) *BIT {
	return &BIT{
		size:   n,
		tree_1: make(map[int]int),
		tree_2: make(map[int]int),
	}
}

func (bit *BIT) _add(idx, delta int) {
	idx++
	i := idx
	for idx <= bit.size {
		bit.tree_1[idx] += delta
		bit.tree_2[idx] += (i - 1) * delta
		idx += idx & -idx
	}
}

func (bit *BIT) add(l, r, delta int) {
	bit._add(l, delta)
	bit._add(r+1, -delta)
}

func (bit *BIT) _query(idx int) int {
	idx++
	if idx > bit.size {
		idx = bit.size
	}

	res, i := 0, idx
	for idx > 0 {
		res += i*bit.tree_1[idx] - bit.tree_2[idx]
		idx -= idx & -idx
	}

	return res
}

func (bit *BIT) query(l, r int) int {
	return bit._query(r) - bit._query(l-1)
}

func sumCounts(nums []int) int {
	result, bit, curr, seen, mod := 0, NewBIT(len(nums)+10), 0, make(map[int]int), int(1e9+7)
	for i, num := range nums {
		j := -1
		if val, ok := seen[num]; ok {
			j = val
		}

		j++
		curr = (curr + bit.query(j, i)*2 + i - j + 1) % mod
		result = (result + curr) % mod
		bit.add(j, i, 1)
		seen[num] = i
	}

	return result
}
