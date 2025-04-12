from typing import Generator
import os
import re

LOG_PATTERN = re.compile(
    r"(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) "
    r"(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL) "
    r"django\.request: .*?(?P<path>/\S+)"
)


def read_logs(paths: list[str]) -> Generator[dict[str, str], None, None]:
    for path in paths:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        with open(path, encoding="utf-8") as f:
            for line in f:
                match = LOG_PATTERN.search(line)
                if match:
                    yield {
                        "path": match.group("path"),
                        "level": match.group("level")
                    }
                else:

                    # Для строк, не подходящих под паттерн django.request
                    if any(level in line for level in ["DEBUG", "WARNING", "CRITICAL"]):
                        yield {
                            "path": "not a django.request",
                            "level": next(level for level in ["DEBUG", "WARNING", "CRITICAL"] if level in line)
                        }