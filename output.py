from typing import Dict, Any


def print_report(report_data: Dict[str, Any]) -> None:
    levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    rows = report_data["rows"]
    totals = report_data["totals"]

    print(f"Total requests: {report_data['total_requests']}\n")
    header = f"{'HANDLER':<24} " + " ".join(f"{lvl:<7}" for lvl in levels)
    print(header)
    for row in rows:
        line = f"{row['path']:<24} " + " ".join(f"{row.get(lvl, 0):<7}" for lvl in levels)
        print(line)
    print(f"{'':<24} " + " ".join(f"{totals[lvl]:<7}" for lvl in levels))
