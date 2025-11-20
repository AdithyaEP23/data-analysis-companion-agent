def check_outputs(report_text, chart_paths):
    issues = []

    if not report_text or len(report_text.strip()) < 50:
        issues.append("Report too short or missing.")

    if not chart_paths:
        issues.append("No charts generated.")

    return "PASS" if not issues else "FAIL: " + "; ".join(issues)
