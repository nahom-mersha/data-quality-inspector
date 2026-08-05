from data_quality_inspector.statistics.manual import mean, standard_deviation


def min_max_scale(values: list[float]) -> list[float]:
    """Scale values to the range 0 to 1."""
    if not values:
        raise ValueError("min-max scaling requires at least one value")

    minimum = min(values)
    maximum = max(values)

    if minimum == maximum:
        raise ValueError(
            "min-max scaling requires values with different minimum and maximum"
        )

    return [(value - minimum) / (maximum - minimum) for value in values]


def standardize(values: list[float]) -> list[float]:
    """Standardize values to have mean 0 and standard deviation 1."""
    if not values:
        raise ValueError("standardization requires at least one value")

    average = mean(values)
    spread = standard_deviation(values)

    if spread == 0:
        raise ValueError(
            "standardization requires values with non-zero standard deviation"
        )

    return [(value - average) / spread for value in values]


import random
from typing import TypeVar

T = TypeVar("T")


def train_test_split(
    values: list[T],
    test_size: float = 0.2,
    random_seed: int | None = None,
) -> tuple[list[T], list[T]]:
    """Split values into training and test sets."""
    if not values:
        raise ValueError("train/test split requires at least one value")

    if not 0 < test_size < 1:
        raise ValueError("test size must be between 0 and 1")

    shuffled_values = values.copy()
    random_generator = random.Random(random_seed)
    random_generator.shuffle(shuffled_values)

    test_count = round(len(values) * test_size)

    if test_count == 0 or test_count == len(values):
        raise ValueError("test size creates an empty train or test set")

    test_values = shuffled_values[:test_count]
    train_values = shuffled_values[test_count:]

    return train_values, test_values
