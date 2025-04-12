from .handlers import HandlersReport

REPORTS = {
    "handlers": HandlersReport
}

def get_report(name: str):
    if name not in REPORTS:
        raise ValueError(f"Unknown report: {name}")
    return REPORTS[name]
