"""
RECORD CHECK  -  my version
===========================

Name  :Ismail joma mohammad
Lane  : IT
Date  :01/11/2026

Run it:   mini_project_week03.py
"""

def status_of(percent, warning_at=90):
    """Return OVER LIMIT, WARNING or OK for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference (limit - value) and the percentage of the limit."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


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


# ---------- Main program ----------
over_limit_count = 0

while True:
    # INPUT
    hostname = input("Hostname (or quit): ")
    if hostname == "quit":
        break
    used = float(input("GB used: "))
    total = float(input("GB total: "))

    # PROCESS
    free, percent = check(used, total)
    status = status_of(percent)

    # OUTPUT
    print_report(hostname, used, total, free, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1

print("Servers over limit:", over_limit_count)