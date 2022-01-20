# PROBLEM STATEMENT
# https://leetcode.com/problems/top-k-frequent-elements/
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.topKFrequentMinHeap(nums, k)

    # Time Complexity: O(n) where n is the size of nums
    # Space Complexity: O(n)
    def topKFrequentList(self, nums: List[int], k: int) -> List[int]:
        item_count_dict = {}
        for n in nums:
            item_count_dict[n] = item_count_dict.get(n, 0) + 1

        count_items_list = [[] for _ in range(len(nums) + 1)]
        for item, count in item_count_dict.items():
            count_items_list[count].append(item)

        result_list = []
        for i in range(len(count_items_list) - 1, -1, -1):
            for item in count_items_list[i]:
                result_list.append(item)
                if len(result_list) == k:
                    return result_list

        return result_list

    # Time Complexity: O(n log k) where n is the size of nums and k is the input k
    #                  O(n) for populating hashmap, O(n log k) for populating heap, O(k) for mapping heap to list
    # Space Complexity: O(n)
    #                   O(n) for hashmap, O(k) for heap, n > k
    def topKFrequentMinHeap(self, nums: List[int], k: int) -> List[int]:
        item_count_dict = {}

        for n in nums:
            item_count_dict[n] = item_count_dict.get(n, 0) + 1

        heap_tuple_list = []
        for item, count in item_count_dict.items():
            heappush(heap_tuple_list, (count, item))

            if len(heap_tuple_list) > k:
                heappop(heap_tuple_list)

        result_list = map(lambda x: x[1], heap_tuple_list)
        return result_list
