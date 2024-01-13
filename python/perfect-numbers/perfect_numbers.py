def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not number > 0:
        raise ValueError("Classification is only possible for positive integers.")

    factors = find_factors(number)[:-1]
    if sum(factors) == number:
        return "perfect"
    elif sum(factors) > number:
        return "abundant"
    elif sum(factors) < number:
        return "deficient"

def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors
