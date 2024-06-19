# https://leetcode.com/problems/peaks-in-array/description/
# 3187. Peaks in Array

from typing import List

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def is_peak(self, i):
        if i <= 0 or i >= self.n - 1:
            return False
        return self.nums[i] > self.nums[i - 1] and self.nums[i] > self.nums[i + 1]

    def build(self, node, start, end):
        if start == end:
            if self.is_peak(start):
                self.tree[node] = 1
            else:
                self.tree[node] = 0
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(left_child, start, mid)
            self.build(right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, node, start, end, idx):
        if start == end:
            if self.is_peak(start):
                self.tree[node] = 1
            else:
                self.tree[node] = 0
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= idx <= mid:
                self.update(left_child, start, mid, idx)
            else:
                self.update(right_child, mid + 1, end, idx)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, node, start, end, L, R):
        if R < start or end < L:
            return 0
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_sum = self.query(left_child, start, mid, L, R)
        right_sum = self.query(right_child, mid + 1, end, L, R)
        return left_sum + right_sum

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        st = SegmentTree(nums)
        result = []

        for query in queries:
            if query[0] == 1:
                li, ri = query[1], query[2]
                result.append(st.query(0, 0, st.n - 1, li + 1, ri - 1))
            elif query[0] == 2:
                indexi, vali = query[1], query[2]
                nums[indexi] = vali
                st.update(0, 0, st.n - 1, indexi)
                if indexi > 0:
                    st.update(0, 0, st.n - 1, indexi - 1)
                if indexi < st.n - 1:
                    st.update(0, 0, st.n - 1, indexi + 1)

        return result
   