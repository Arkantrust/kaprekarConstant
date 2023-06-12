"""For any 4-digit number with at least 2 different digits. If arranged in descending and ascending order and subtracted,
eventually we will get Kaprekar's constant = 6174.
"""

KAPREKAR_CONSTANT = 6174


def int_to_list(num: str) -> list[str]:
    return [num[n] for n in range(4)]


def has_different_digits(number_string: str) -> bool:
    has_different = True
    for digit in range(3):
        current_digit = number_string[digit]
        next_digit = number_string[digit + 1]
        if current_digit != next_digit:
            has_different = True
        else:
            has_different = False
            break
    return has_different


def subtract_ordered_lists(minuend_list: list[str], subtrahend_list: list[str]) -> int:
    minuend_str = ''.join(minuend_list)
    subtrahend_str = ''.join(subtrahend_list)
    return int(minuend_str) - int(subtrahend_str)


def perform_iteration(number: int) -> int:
    number = str(number)
    digits_list = int_to_list(number)
    descending_list = sorted(digits_list, reverse=True)
    ascending_list = sorted(digits_list)
    result = subtract_ordered_lists(descending_list, ascending_list)
    return result


def kaprekar(candidate: int) -> str:

    number = candidate
    iterations = 0

    while number != KAPREKAR_CONSTANT:
        number = perform_iteration(number)
        iterations += 1
    return f"The number {candidate} reaches Kaprekar's constant after {iterations} iterations"


# Testing
data = [3524, 7238, 9823, 2323, 1234, 5678, 9012, 3456, 7890, 9876]

for num in data:
    print(kaprekar(num))
