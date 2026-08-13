class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        s = list(s)
        n = len(s)
        tree = [[0, 0, 0] for _ in range(4 * n)]

        def merge(node, l, r):
            mid = (l + r) // 2
            left = tree[node * 2]
            right = tree[node * 2 + 1]

            pref = left[0]
            suff = right[1]
            best = max(left[2], right[2])

            if s[mid] == s[mid + 1]:
                if left[0] == mid - l + 1:
                    pref += right[0]
                if right[1] == r - mid:
                    suff += left[1]
                best = max(best, left[1] + right[0])

            tree[node] = [pref, suff, best]

        def build(node, l, r):
            if l == r:
                tree[node] = [1, 1, 1]
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            merge(node, l, r)

        def update(node, l, r, idx):
            if l == r:
                tree[node] = [1, 1, 1]
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx)
            else:
                update(node * 2 + 1, mid + 1, r, idx)

            merge(node, l, r)

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            s[idx] = ch
            update(1, 0, n - 1, idx)
            ans.append(tree[1][2])

        return ans