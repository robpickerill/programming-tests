def reverse_number(nums: int) -> int:
    result = 0

    while nums > 0:
        remainder = nums % 10
        result = (result * 10) + remainder
        nums //= 10

    return result


assert reverse_number(12345) == 54321
