from collections import defaultdict
from typing import Dict, Any

LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class HandlersReport:
    def __init__(self):
        self.data = defaultdict(lambda: defaultdict(int))
        self.total = 0

    def process(self, entry: dict[str, str]) -> None:
        path = entry["path"]
        level = entry["level"]
        if level in LEVELS:
            self.data[path][level] += 1
            self.total += 1

    def generate(self) -> Dict[str, Any]:
        result = {
            "rows": [],
            "totals": {level: 0 for level in LEVELS},
            "total_requests": self.total
        }

        for path in sorted(self.data):
            row = {"path": path}
            for level in LEVELS:
                count = self.data[path].get(level, 0)
                row[level] = count
                result["totals"][level] += count
            result["rows"].append(row)

        return result
