def kaprekar(candidate: int) -> int | None:
    """
    The `kaprekar` function takes an integer `candidate` and returns the number of
    iterations it takes to reach the Kaprekar constant 6174.

    :param candidate: The `candidate` parameter is an integer representing the number
    for which we want to find the number of iterations required to reach the
    Kaprekar's constant
    :type candidate: int
    :return: The function `kaprekar` returns the number of iterations it takes
    for the given candidate number to reach the Kaprekar's constant 6174.
    """
    if candidate < 1000 or candidate > 9999 or len(set(str(candidate))) < 2:
        return None

    number = candidate
    iterations = 0

    while number != 6174:
        number_str = str(number)
        number = int("".join(sorted(number_str, reverse=True))) - int(
            "".join(sorted(number_str))
        )
        iterations += 1

    return iterations
