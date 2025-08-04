def find_unique_value(numbers: list[int]) -> int | None:
    for number in numbers:
        if numbers.count(number) == 1:
            return number
    return None


print(find_unique_value([]))



assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
