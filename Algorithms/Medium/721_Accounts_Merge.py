from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
            
    def find(self, x: int) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
                
        return self.parents[x]
            
    def union(self, child: int, parent: int) -> None:
        self.parents[self.find(child)] = self.find(parent)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        ownership = {}

        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email in ownership:
                    uf.union(i, ownership[email])
                
                ownership[email] = i
        
        result = defaultdict(list)
        for email, owner in ownership.items():
            result[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in result.items()]
