"""
For any 4-digit number with at least 2 different digits. If arranged in descending and ascending order and subtracted,
eventually we will get Kaprekar's constant = 6174.
"""

KAPREKAR_CONSTANT = 6174


def kaprekar(candidate: int) -> str:
    """
    The function takes an integer input and returns the number of iterations it takes to reach
    Kaprekar's constant.

    :param candidate: an integer that represents the starting number for the Kaprekar's constant
    algorithm. The function will iterate on this number until it reaches the Kaprekar's constant
    :type candidate: int
    :return: The function `kaprekar` returns a string that states how many iterations it takes for a
    given number to reach Kaprekar's constant. The string includes the original number and the number of
    iterations.
    """

    if candidate < 1000 or candidate > 9999 or not len(set(str(candidate))) >= 2:
        return f"The number must be a 4-digit integer with at least 2 different digits"
    elif candidate == KAPREKAR_CONSTANT:
        return f"The number {candidate} is already Kaprekar's constant"

    number = candidate
    iterations = 0

    while number != KAPREKAR_CONSTANT:
        number_str = str(number)
        number = int(''.join(sorted(number_str, reverse=True))) - int(''.join(sorted(number_str)))
        iterations += 1
    return f"The number {candidate} reaches Kaprekar's constant after {iterations} iterations"
