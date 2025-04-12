from reports.handlers import HandlersReport


def test_handlers_report_processing():
    report = HandlersReport()
    report.process({"path": "/test/", "level": "INFO"})
    report.process({"path": "/test/", "level": "INFO"})
    report.process({"path": "/test/", "level": "ERROR"})
    data = report.generate()
    assert data["total_requests"] == 3
    assert data["totals"]["INFO"] == 2
    assert data["totals"]["ERROR"] == 1
    assert data["rows"][0]["path"] == "/test/"
