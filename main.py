from cli import parse_args
from log_reader import read_logs
from reports import get_report
from output import print_report
import sys


def main() -> None:
    args = parse_args()

    try:
        report_class = get_report(args.report)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        log_entries = read_logs(args.log_files)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    report = report_class()
    for entry in log_entries:
        report.process(entry)

    print_report(report.generate())


if __name__ == "__main__":
    main()
