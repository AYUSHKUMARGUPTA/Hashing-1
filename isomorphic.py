# Time Complexity: O(n) To iterate through both the string s and t
# Space Complexity: O(n) Created 2 hashmap to store the mapping which will be of 2*26
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t:
            return False

        if len(s) != len(t):
            return False

        mapST, mapTS = {}, {}

        for c1, c2 in zip(s,t):
            if ((c1 in mapST and mapST[c1]!=c2) or 
            (c2 in mapTS and mapTS[c2]!=c1)):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1

        return True