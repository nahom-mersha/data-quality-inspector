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
