def calculate_percentage(part, whole):

    if part is None or whole is None:
        return None

    if whole == 0:
        return None

    per = (part / whole) * 100
    return per


def calculate_average(numbers):

    if numbers is None or len(numbers) == 0:
        return None

    ava = sum(numbers) / len(numbers)
    return ava


def find_max_min(numbers):

    if numbers is None or len(numbers) == 0:
        return None

    maximum = max(numbers)
    minimum = min(numbers)

    return maximum, minimum


def is_prime(n):

    if n is None or n <= 1:
        return False

    for number in range(2, n):
        if n % number == 0:
            return False

    return True