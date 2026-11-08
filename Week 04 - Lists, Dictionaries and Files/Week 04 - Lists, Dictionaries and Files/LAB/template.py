"""
RECORD CHECK  -  my version
===========================

Name  :Ismail joma mohmaad
Lane  :IT
Date  :01/11/2026

Run it:   Mini_project_week4.py

"""


def status_of(percent, warning_at=90):
    """Return OVER LIMIT, WARNING or OK for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"


def check_record(used, total):
    """Return the free space and the percentage used."""
    free = total - used
    percent = (used / total) * 100
    return free, percent


def print_report(hostname, used, total, free, percent, status):
    """Print the bordered report for one server."""
    line = "=" * 34
    print(line)
    print(f"  RECORD CHECK  -  {hostname}")
    print(line)
    print(f"  {'Used':<10} : {used:>10.2f}")
    print(f"  {'Total':<10} : {total:>10.2f}")
    print(f"  {'Free':<10} : {free:>10.2f}")
    print(f"  {'Percent':<10} : {percent:>10.2f} %")
    print(f"  {'Status':<10} : {status:>10}")
    print(line)


# ---------- Records: a list of tuples (hostname, GB used, GB total) ----------
records = [
    ("srv-01", 87, 120),
    ("srv-02", 110, 120),
    ("srv-03", 125, 120),
]

# ---------- Main program ----------
for record in records:
    hostname = record[0]
    used = record[1]
    total = record[2]

    free, percent = check_record(used, total)
    status = status_of(percent)

    print_report(hostname, used, total, free, percent, status)


