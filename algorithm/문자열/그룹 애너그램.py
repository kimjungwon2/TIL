from collections import Counter, defaultdict


class Solution(object):
    def groupAnagrams(self, strs):

        a = defaultdict(list)

        for str in strs:
            a[''.join(sorted(str))].append(str)

        return a.values()
