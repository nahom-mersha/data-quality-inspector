import numpy as np


def mean(values: list[float]) -> float:
    """Return the arithmetic mean of non-empty values using NumPy."""
    if not values:
        raise ValueError("mean requires at least one value")

    return float(np.mean(values))


def median(values: list[float]) -> float:
    """Return the median of non-empty values using NumPy."""
    if not values:
        raise ValueError("median requires at least one value")

    return float(np.median(values))


def variance(values: list[float]) -> float:
    """Return the population variance of non-empty values using NumPy."""
    if not values:
        raise ValueError("variance requires at least one value")

    return float(np.var(values))


def standard_deviation(values: list[float]) -> float:
    """Return the population standard deviation of non-empty values using NumPy."""
    if not values:
        raise ValueError("standard deviation requires at least one value")

    return float(np.std(values))


def quantile(values: list[float], proportion: float) -> float:
    """Return a quantile from 0 to 1 for non-empty values using NumPy."""
    if not values:
        raise ValueError("quantile requires at least one value")

    if not 0 <= proportion <= 1:
        raise ValueError("quantile proportion must be between 0 and 1")

    return float(np.quantile(values, proportion))


def z_score(value: float, values: list[float]) -> float:
    """Return how many standard deviations value is from the mean using NumPy."""
    average = mean(values)
    spread = standard_deviation(values)

    if spread == 0:
        raise ValueError("z-score cannot be calculated when standard deviation is zero")

    return float((value - average) / spread)
