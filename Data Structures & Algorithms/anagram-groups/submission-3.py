
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = defaultdict(list) # sorted anagrams: list of words

        for word in strs:
            key = ".".join(sorted(word))
            g[key].append(word)
        return list(g.values())

        
            
