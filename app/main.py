def format_linter_error(error: dict) -> dict:
    return error


def format_linter_errors(errors: list) -> dict:
    return {"errors": errors}


def format_linter_report(linter_report: dict) -> list:
    if isinstance(linter_report, dict):
        if "errors" in linter_report:
            return linter_report["errors"]
        flattened = []
        for value in linter_report.values():
            if isinstance(value, list):
                flattened.extend(value)
        if flattened:
            return flattened
    # fallback: coerce iterable to list
    try:
        return list(linter_report)
    except TypeError:
        return []
