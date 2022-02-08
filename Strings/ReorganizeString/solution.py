# PROBLEM STATEMENT
# https://leetcode.com/problems/reorganize-string/
# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# Return any possible rearrangement of s or return "" if not possible.

class Solution:
    def reorganizeString(self, s: str) -> str:
        return self.reorganizeStringsHeap(s)

    # Time Complexity: O(n log n) where n is the length of str
    # Space Complexity: O(n)
    def reorganizeStringsHeap(self, s: str) -> str:
        import heapq
        counter = {}
        for c in s:
            # counter[c] = counter[c] + 1 if c in counter else 1
            counter[c] = counter.get(c, 0) + 1

        heap = [[-count, ch] for ch, count in counter.items()]

        heapq.heapify(heap)
        prev = None
        result = ""

        while heap or prev:
            if not heap and prev:
                return ""

            count, ch = heapq.heappop(heap)
            count += 1
            result += ch

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if count:
                prev = [count, ch]

        return result

