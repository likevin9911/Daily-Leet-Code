from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return True
        return False

def main():
    arr = [1, 2, 3, 5, 7, 2, 4, 9, 11, 13]
    solution = Solution()
    if solution.threeConsecutiveOdds(arr):
        print("True.")
    else:
        print("False.")

if __name__ == "__main__":
    main()
