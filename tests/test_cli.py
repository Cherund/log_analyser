from cli import parse_args
import sys


def test_parse_args(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main.py", "file1.log", "--report", "handlers"])
    args = parse_args()
    assert args.log_files == ["file1.log"]
    assert args.report == "handlers"
