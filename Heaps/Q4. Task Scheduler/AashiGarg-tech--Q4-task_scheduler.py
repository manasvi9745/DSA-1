class Solution(object):
    def leastInterval(self, tasks, n):
        from collections import Counter

        freq = Counter(tasks)

        max_freq = max(freq.values())
        count_max = sum(1 for v in freq.values() if v == max_freq)

        part = (max_freq - 1) * (n + 1) + count_max

        return max(len(tasks), part)
