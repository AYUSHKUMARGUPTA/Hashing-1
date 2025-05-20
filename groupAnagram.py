# Time Complexity: O(n * k), n = number of strings, k = average length of strings
# Space Complexity: O(n * k), for storing results in a hashmap and the final list of groups.
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        if not strs:
            return []

        # Assign prime numbers to each alphabet
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                  41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        
        def calculate_product(s: str) -> int:
            product = 1
            for char in s:
                product *= primes[ord(char) - ord('a')]
            return product
        
        hashmap = defaultdict(list)
        
        for s in strs:
            key = calculate_product(s)
            hashmap[key].append(s)
        
        return list(hashmap.values())