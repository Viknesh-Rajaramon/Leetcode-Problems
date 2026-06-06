package main

type TrieNode map[rune]interface{}

type Trie struct {
	root TrieNode
}

func newTrie() *Trie {
	return &Trie{root: make(TrieNode)}
}

func less(a, b [2]int) bool {
	if a[0] < b[0] {
		return true
	} else if a[0] == b[0] {
		return a[1] < b[1]
	}

	return false
}

func (t *Trie) insert(s string, idx int) {
	node := t.root
	best := [2]int{len(s), idx}

	if val, ok := node['#']; !ok || less(best, val.([2]int)) {
		node['#'] = best
	}

	for _, c := range s {
		if _, ok := node[c]; !ok {
			node[c] = make(TrieNode)
		}

		node = node[c].(TrieNode)
		if val, ok := node['#']; !ok || less(best, val.([2]int)) {
			node['#'] = best
		}
	}
}

func (t *Trie) query(s string) int {
	node := t.root
	for _, c := range s {
		if next, ok := node[c]; ok {
			node = next.(TrieNode)
		} else {
			break
		}
	}

	return node['#'].([2]int)[1]
}

func stringIndices(wordsContainer []string, wordsQuery []string) []int {
	trie := newTrie()
	for i, word := range wordsContainer {
		runes := []rune(word)
		for l, r := 0, len(runes)-1; l < r; l, r = l+1, r-1 {
			runes[l], runes[r] = runes[r], runes[l]
		}

		trie.insert(string(runes), i)
	}

	result := make([]int, len(wordsQuery))
	for i, query := range wordsQuery {
		runes := []rune(query)
		for l, r := 0, len(runes)-1; l < r; l, r = l+1, r-1 {
			runes[l], runes[r] = runes[r], runes[l]
		}

		result[i] = trie.query(string(runes))
	}

	return result
}
