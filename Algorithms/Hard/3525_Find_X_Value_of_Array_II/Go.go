package main

type SegmentTree struct {
	k    int
	tree [][]int
}

func bitsLen(n int) int {
	cnt := 0
	for n > 0 {
		cnt++
		n >>= 1
	}

	return cnt
}

func NewSegmentTree(nums []int, k int) *SegmentTree {
	n := len(nums)
	tree := make([][]int, 1<<(bitsLen(n)+1))
	for i := range tree {
		tree[i] = make([]int, k+1)
	}

	st := &SegmentTree{k: k, tree: tree}
	st.build(nums, 1, 0, n-1)
	return st
}

func (st *SegmentTree) make_leaf(o, value int) {
	info, r := make([]int, st.k+1), value%st.k
	info[r], info[st.k] = 1, r
	st.tree[o] = info
}

func (st *SegmentTree) merge_pre(left, right []int) []int {
	pre := make([]int, st.k+1)
	pre[st.k] = (left[st.k] * right[st.k]) % st.k
	for x := range st.k {
		pre[x] = left[x]
	}

	for x := range st.k {
		pre[(left[st.k]*x)%st.k] += right[x]
	}

	return pre
}

func (st *SegmentTree) build(nums []int, o, l, r int) {
	if l == r {
		st.make_leaf(o, nums[l])
		return
	}

	m := (l + r) >> 1
	st.build(nums, o<<1, l, m)
	st.build(nums, (o<<1)|1, m+1, r)
	st.tree[o] = st.merge_pre(st.tree[o<<1], st.tree[(o<<1)|1])
}

func (st *SegmentTree) update(o, l, r, index, value int) {
	if l == r {
		st.make_leaf(o, value)
		return
	}

	m := (l + r) >> 1
	if index <= m {
		st.update(o<<1, l, m, index, value)
	} else {
		st.update((o<<1)|1, m+1, r, index, value)
	}

	st.tree[o] = st.merge_pre(st.tree[o<<1], st.tree[(o<<1)|1])
}

func (st *SegmentTree) query(o, l, r, L, R int) []int {
	if L <= l && r <= R {
		return st.tree[o]
	}

	m := (l + r) >> 1
	if R <= m {
		return st.query(o<<1, l, m, L, R)
	}

	if L > m {
		return st.query((o<<1)|1, m+1, r, L, R)
	}

	return st.merge_pre(st.query(o<<1, l, m, L, R), st.query((o<<1)|1, m+1, r, L, R))
}

func resultArray(nums []int, k int, queries [][]int) []int {
	result, n, st := make([]int, 0), len(nums), NewSegmentTree(nums, k)
	for _, q := range queries {
		index, value, start, x := q[0], q[1], q[2], q[3]
		st.update(1, 0, n-1, index, value)
		result = append(result, st.query(1, 0, n-1, start, n-1)[x])
	}

	return result
}
