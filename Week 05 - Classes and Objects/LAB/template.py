"""
RECORD CHECK  -  my version
===========================

Name  :Ismail joma mohammad 
Lane  :IT      
Date  :5/11/2026

Run it:   Mini_Project_Week05.py

"""


class Record:
    def __init__(self, label, value, limit):
        self.label = label      # hostname
        self.value = value      # GB used
        self.limit = limit      # GB total

    def status(self):
        """Return OVER LIMIT, WARNING or OK for this record."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


def print_report(record, status):
    """Print the bordered report for one record."""
    line = "=" * 34
    print(line)
    print(f"  RECORD CHECK  -  {record.label}")
    print(line)
    print(f"  {'Used':<10} : {record.value:>10.2f}")
    print(f"  {'Total':<10} : {record.limit:>10.2f}")
    print(f"  {'Status':<10} : {status:>10}")
    print(line)


# ---------- Create the objects ----------
r1 = Record("srv-01", 87.0, 120.0)
r2 = Record("srv-02", 110.0, 120.0)
r3 = Record("srv-03", 125.0, 120.0)

# ---------- Call status() once per record, store it, then use it ----------
status1 = r1.status()
status2 = r2.status()
status3 = r3.status()

print_report(r1, status1)
print_report(r2, status2)
print_report(r3, status3)

# ---------- Check the objects are independent ----------
r1.value = 95.0
print(r1.value, r2.value)   # r1 changed, r2 did not