import pytest

from data_quality_inspector.preprocessing import (
    min_max_scale,
    standardize,
    train_test_split,
)


def test_min_max_scale_scales_values_between_zero_and_one() -> None:
    assert min_max_scale([10, 20, 30]) == [0.0, 0.5, 1.0]


def test_min_max_scale_handles_negative_values() -> None:
    assert min_max_scale([-10, 0, 10]) == [0.0, 0.5, 1.0]


def test_min_max_scale_rejects_empty_list() -> None:
    with pytest.raises(ValueError, match="at least one value"):
        min_max_scale([])


def test_min_max_scale_rejects_values_with_no_range() -> None:
    with pytest.raises(ValueError, match="different minimum and maximum"):
        min_max_scale([5, 5, 5])


def test_standardize_centers_values_around_zero() -> None:
    assert standardize([2, 4, 6, 8]) == pytest.approx(
        [-1.3416408, -0.4472136, 0.4472136, 1.3416408]
    )


def test_standardize_rejects_empty_list() -> None:
    with pytest.raises(ValueError, match="at least one value"):
        standardize([])


def test_standardize_rejects_values_with_no_spread() -> None:
    with pytest.raises(ValueError, match="non-zero standard deviation"):
        standardize([5, 5, 5])


def test_train_test_split_splits_values() -> None:
    train, test = train_test_split([1, 2, 3, 4, 5], test_size=0.4, random_seed=42)

    assert len(train) == 3
    assert len(test) == 2
    assert sorted(train + test) == [1, 2, 3, 4, 5]


def test_train_test_split_is_reproducible_with_seed() -> None:
    first_train, first_test = train_test_split([1, 2, 3, 4, 5], random_seed=42)
    second_train, second_test = train_test_split([1, 2, 3, 4, 5], random_seed=42)

    assert first_train == second_train
    assert first_test == second_test


def test_train_test_split_rejects_empty_list() -> None:
    with pytest.raises(ValueError, match="at least one value"):
        train_test_split([])


def test_train_test_split_rejects_invalid_test_size() -> None:
    with pytest.raises(ValueError, match="between 0 and 1"):
        train_test_split([1, 2, 3], test_size=1.5)
