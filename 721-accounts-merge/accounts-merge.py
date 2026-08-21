class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        uf = UnionFind(len(accounts))
        email_to_account = {}

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email_to_account:
                    uf.union(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        merged = {}
        for email, acc_idx in email_to_account.items():
            leader = uf.find(acc_idx)
            if leader not in merged:
                merged[leader] = []
            merged[leader].append(email)

        result = []
        for leader, emails in merged.items():
            result.append([accounts[leader][0]] + sorted(emails))

        return result