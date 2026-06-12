class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            count = Counter(word)
            key_count = frozenset(count.items())
            groups.setdefault(key_count, []).append(word)
        
        return [groups[group] for group in groups]