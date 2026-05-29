class Trie {
public:
    Trie* child[26];
    pair<int, int> best;

    Trie() {
        memset(child, 0, sizeof(child));
        best = {INT_MAX, INT_MAX};
    }

    void insert(const string& s, int idx) {
        Trie* node = this;
        pair<int, int> curr_best = {(int)s.size(), idx};
        if (curr_best < node->best)
            node->best = curr_best;
        
        for (char c : s) {
            int x = c-'a';
            if (!node->child[x])
                node->child[x] = new Trie();
            
            node = node->child[x];
            if (curr_best < node->best)
                node->best = curr_best;
        }
    }

    int query(const string& s) {
        Trie* node = this;
        for (char c : s) {
            int x = c - 'a';
            if (!node->child[x])
                break;
            
            node = node->child[x];
        }

        return node->best.second;
    }
};

class Solution {
public:
    vector<int> stringIndices(vector<string>& wordsContainer, vector<string>& wordsQuery) {
        Trie trie;
        for (int i=0; i<wordsContainer.size(); ++i) {
            string word = wordsContainer[i];
            reverse(word.begin(), word.end());
            trie.insert(word, i);
        }

        vector<int> result;
        for (int i=0; i<wordsQuery.size(); ++i) {
            string query = wordsQuery[i];
            reverse(query.begin(), query.end());
            result.push_back(trie.query(query));
        }

        return result;
    }
};
