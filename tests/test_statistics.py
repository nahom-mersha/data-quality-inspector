import pytest

from data_quality_inspector.statistics.manual import (
    mean,
    median,
    quantile,
    standard_deviation,
    variance,
    z_score,
)


def test_mean_returns_average() -> None:
    assert mean([2, 4, 6, 8]) == 5.0


def test_mean_rejects_empty_list() -> None:
    with pytest.raises(ValueError, match="at least one value"):
        mean([])


def test_median_returns_middle_value_for_odd_count() -> None:
    assert median([8, 2, 4]) == 4.0


def test_median_returns_average_of_middle_values_for_even_count() -> None:
    assert median([8, 2, 6, 4]) == 5.0


def test_median_rejects_empty_list() -> None:
    with pytest.raises(ValueError, match="at least one value"):
        median([])


def test_variance_measures_spread() -> None:
    assert variance([2, 4, 6, 8]) == 5.0


def test_variance_is_zero_when_all_values_match() -> None:
    assert variance([3, 3, 3]) == 0.0


def test_variance_rejects_empty_list() -> None:
    with pytest.raises(ValueError, match="at least one value"):
        variance([])


def test_standard_deviation_measures_typical_spread() -> None:
    assert standard_deviation([2, 4, 6, 8]) == pytest.approx(2.2360679)


def test_standard_deviation_is_zero_when_all_values_match() -> None:
    assert standard_deviation([3, 3, 3]) == 0.0


def test_standard_deviation_rejects_empty_list() -> None:
    with pytest.raises(ValueError, match="at least one value"):
        standard_deviation([])


def test_quantile_returns_25th_percentile() -> None:
    assert quantile([2, 4, 6, 8], 0.25) == 3.5


def test_quantile_returns_median_at_50_percent() -> None:
    assert quantile([2, 4, 6, 8], 0.50) == 5.0


def test_quantile_returns_75th_percentile() -> None:
    assert quantile([2, 4, 6, 8], 0.75) == 6.5


def test_quantile_rejects_empty_list() -> None:
    with pytest.raises(ValueError, match="at least one value"):
        quantile([], 0.25)


def test_quantile_rejects_invalid_proportion() -> None:
    with pytest.raises(ValueError, match="between 0 and 1"):
        quantile([2, 4, 6, 8], 1.5)


def test_z_score_measures_distance_from_mean() -> None:
    assert z_score(8, [2, 4, 6, 8]) == pytest.approx(1.3416408)


def test_z_score_is_zero_at_the_mean() -> None:
    assert z_score(5, [2, 4, 6, 8]) == 0.0


def test_z_score_rejects_values_with_no_spread() -> None:
    with pytest.raises(ValueError, match="standard deviation is zero"):
        z_score(3, [3, 3, 3])
