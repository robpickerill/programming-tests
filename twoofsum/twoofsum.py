from typing import Dict, List


def twosum(n: List[int], t: int) -> List[int]:
    comp: Dict[int, int] = dict()

    for i, v in enumerate(n):
        second = t - v

        if second in comp.keys():
            return [comp[second], i]
        else:
            comp[v] = i

    return []


n = [4, 5, 6, 4]
t = 8

print(twosum(n, t))


n = [4, 5, 6, 4]
t = 9

print(twosum(n, t))


n = [4, 5, 6, 4]
t = 200

print(twosum(n, t))
