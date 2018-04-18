def equal_split_index(arr):
    # type: Sequence[int] -> Maybe[int]
    """Splits a sequence of ints into two segments with equal sums

    Returns the minimum index ``i`` such that:
      ``0 <= i <= len(arr) and sum(arr[:i]) == sum(arr[i:])``

    Returns ``None`` if there is no such ``i``.
    """

    left_sum = 0
    right_sum = sum(arr)

    # if the total sum of the sequence is 0 then an empty left
    # subsequence is always the first valid solution.
    if right_sum == 0:
        return 0

    for i, val in enumerate(arr, 1):
        left_sum += val
        right_sum -= val
        if left_sum == right_sum:
            return i

    return None
