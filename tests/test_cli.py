import sys

import pytest

from data_quality_inspector.__main__ import main


def test_missing_file_shows_clear_error(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["data_quality_inspector", "not_a_real_file.csv"],
    )

    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 2

    captured = capsys.readouterr()
    assert "File not found: not_a_real_file.csv" in captured.err


def test_duplicate_rows_are_reported(
    monkeypatch,
    capsys,
    tmp_path,
) -> None:
    csv_file = tmp_path / "people.csv"

    csv_file.write_text(
        "age,income,city,student\n22,25000,Berlin,no\n22,25000,Berlin,no\n"
    )

    monkeypatch.setattr(
        sys,
        "argv",
        ["data_quality_inspector", str(csv_file)],
    )

    main()

    captured = capsys.readouterr()

    assert "Duplicate rows: 1" in captured.out


def test_constant_columns_are_reported(
    monkeypatch,
    capsys,
    tmp_path,
) -> None:
    csv_file = tmp_path / "people.csv"

    csv_file.write_text("name,age,country\nAnna,21,Germany\nBen,22,Germany\n")

    monkeypatch.setattr(
        sys,
        "argv",
        ["data_quality_inspector", str(csv_file)],
    )

    main()

    captured = capsys.readouterr()

    assert "Constant columns:" in captured.out
    assert "- country: Germany" in captured.out


def test_invalid_age_values_are_reported(
    monkeypatch,
    capsys,
    tmp_path,
) -> None:
    csv_file = tmp_path / "people.csv"

    csv_file.write_text("name,age\nAnna,22\nJohn,-5\nSara,unknown\nMia,\nLeo,150\n")

    monkeypatch.setattr(
        sys,
        "argv",
        ["data_quality_inspector", str(csv_file)],
    )

    main()

    captured = capsys.readouterr()

    assert "Suspicious values:" in captured.out
    assert "- age: 1 non-numeric value(s)" in captured.out
    assert "- age: 1 value(s) below the allowed minimum of 0" in captured.out
    assert "- age: 1 value(s) above the allowed maximum of 120" in captured.out
