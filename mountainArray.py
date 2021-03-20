class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        peak = 0
        for i in range(1, len(arr) - 2):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                peak += 1
            if arr[i - 1] >= arr[i] <= arr[i + 1]:
                return False
        return peak == 1
            
