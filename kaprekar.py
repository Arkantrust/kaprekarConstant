def kaprekar(candidate: int) -> int:
    """
    The function takes a 4-digit integer with at least 2 different digits and returns the number of
    iterations it takes to reach Kaprekar's constant.

    :param candidate: The input number that we want to check if it can be transformed into Kaprekar's
    constant through a series of operations
    :type candidate: int
    :return: the number of iterations it takes for a given 4-digit integer to reach Kaprekar's constant
    (6174) using the Kaprekar routine. If the input is not a valid 4-digit integer with at least 2
    different digits, an error message is returned.
    """
    if candidate < 1000 or candidate > 9999 or len(set(str(candidate))) < 2:
        return "The number must be a 4-digit integer with at least 2 different digits"

    number = candidate
    iterations = 0

    while number != 6174:
        number_str = str(number)
        number = int("".join(sorted(number_str, reverse=True))) - int("".join(sorted(number_str))
        )
        iterations += 1

    return iterations
