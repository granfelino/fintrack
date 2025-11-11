from fintrack.cli import *
import datetime as dt

def test_input_date(monkeypatch):
    inputs = "2012 12 31"
    monkeypatch.setattr("builtins.input", lambda _: inputs)
    result = input_date()
    assert result == dt.date(2012, 12, 31)

def test_input_date_invalid_args(monkeypatch):
    inputs = iter(["12 12", "2012 12 31"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = input_date()
    assert result == dt.date(2012, 12, 31)

def test_input_date_invalid(monkeypatch):
    inputs = "111 111 111"
    monkeypatch.setattr("builtins.input", lambda _: inputs)
    result = input_date()
    assert result is None
