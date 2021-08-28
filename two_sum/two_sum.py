from typing import Dict, List


def two_sum(nums: List[int], sum: int) -> List[List[int]]:
    dp: Dict[int, int] = dict()
    results: List[List[int]] = list()

    for v in nums:
        tmp = sum - v

        if tmp not in dp:
            dp[v] = v
        else:
            results.append([v, dp[tmp]])

    return results


if __name__ == "__main__":
    assert two_sum([1, 2, 3, 4], 4) == [[3, 1]]
