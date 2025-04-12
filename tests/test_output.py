from output import print_report


def test_print_report(capsys):
    report = {
        "total_requests": 3,
        "totals": {"DEBUG": 0, "INFO": 2, "WARNING": 0, "ERROR": 1, "CRITICAL": 0},
        "rows": [
            {"path": "/test/", "DEBUG": 0, "INFO": 2, "WARNING": 0, "ERROR": 1, "CRITICAL": 0}
        ]
    }
    print_report(report)
    out = capsys.readouterr().out
    assert "Total requests: 3" in out
    assert "/test/" in out
