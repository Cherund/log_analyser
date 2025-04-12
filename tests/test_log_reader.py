from log_reader import read_logs
import tempfile


def test_read_logs_extracts_entries():
    content = (
        '2023-12-01 12:00:00,000 INFO django.request: GET /api/v1/test/\n'
        '2023-12-01 12:01:00,000 ERROR django.request: POST /api/v1/test/\n'
    )
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(content)
        f.flush()
        logs = list(read_logs([f.name]))
    assert len(logs) == 2
    assert logs[0]["path"] == "/api/v1/test/"
    assert logs[0]["level"] == "INFO"
