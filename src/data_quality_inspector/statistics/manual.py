import math


def mean(values: list[float]) -> float:
    """Return the arithmetic mean of non-empty values."""
    if not values:
        raise ValueError("mean requires at least one value")

    return sum(values) / len(values)


def median(values: list[float]) -> float:
    """Return the median of non-empty values."""
    if not values:
        raise ValueError("median requires at least one value")

    sorted_values = sorted(values)
    middle_index = len(sorted_values) // 2

    if len(sorted_values) % 2 == 1:
        return sorted_values[middle_index]

    return (sorted_values[middle_index - 1] + sorted_values[middle_index]) / 2


def variance(values: list[float]) -> float:
    """Return the population variance of non-empty values."""
    if not values:
        raise ValueError("variance requires at least one value")

    average = mean(values)

    squared_distances = [(value - average) ** 2 for value in values]

    return sum(squared_distances) / len(values)


def standard_deviation(values: list[float]) -> float:
    """Return the population standard deviation of non-empty values."""
    if not values:
        raise ValueError("standard deviation requires at least one value")

    return math.sqrt(variance(values))


def quantile(values: list[float], proportion: float) -> float:
    """Return a quantile from 0 to 1 for non-empty values."""
    if not values:
        raise ValueError("quantile requires at least one value")

    if not 0 <= proportion <= 1:
        raise ValueError("quantile proportion must be between 0 and 1")

    sorted_values = sorted(values)
    position = (len(sorted_values) - 1) * proportion

    lower_index = math.floor(position)
    upper_index = math.ceil(position)

    if lower_index == upper_index:
        return sorted_values[lower_index]

    lower_value = sorted_values[lower_index]
    upper_value = sorted_values[upper_index]
    distance_from_lower = position - lower_index

    return lower_value + (upper_value - lower_value) * distance_from_lower


def z_score(value: float, values: list[float]) -> float:
    """Return how many standard deviations value is from the mean."""
    average = mean(values)
    spread = standard_deviation(values)

    if spread == 0:
        raise ValueError("z-score cannot be calculated when standard deviation is zero")

    return (value - average) / spread
