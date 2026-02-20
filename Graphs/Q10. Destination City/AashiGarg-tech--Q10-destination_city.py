class Solution(object):
    def destCity(self, paths):
        starts = set()

        for a, b in paths:
            starts.add(a)

        for a, b in paths:
            if b not in starts:
                return b
