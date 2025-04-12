import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Django log analyzer")
    parser.add_argument("log_files", nargs="+", help="Paths to log files")
    parser.add_argument("--report", required=True, help="Report name, e.g., 'handlers'")
    return parser.parse_args()
