# coding=utf-8
# @Time: 3/6/2019 6:59 PM

# Definition for an interval.
from typing import List


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals.sort(key=lambda x: x.start)
        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged


print(Solution().merge([[1,4],[4,5]]))
