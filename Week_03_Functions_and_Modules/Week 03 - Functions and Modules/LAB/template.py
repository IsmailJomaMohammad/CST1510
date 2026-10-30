"""
RECORD CHECK  -  my version
===========================

Name  : Ismail
Lane  :  IT
Date  : 

Run it:   python template.py


"""

def status_of(percent):
    """return "OVER LIMIT", "WARNING" or "OK" for a given percentage"""
    if percent >= 100:      
        return "OVER LIMIT"
    elif percent >= 90: 
        return "WARNING"
    else:                 
        return "OK"


def check(value, limit):
    """Return the difference and the percentage of value"""
    difference = value - limit   
    percent = (value / limit) * 100
    return difference, percent     


def print_report(label, value, limit, difference, percent, status):
    """print the full bordered report to print one record"""
    print()
    print("=" * 34)
    print(f" RECORD CHECK - {label}")
    print("=" * 34)
    print(f" value: {value:>12.2f}")
    print(f" limit : {limit:>12.2f}")
    print(f" difference: {difference:>12.2f}")
    print(f" percent: {percent:12.2f}")
    print(f" status: {status:>12}")    
    print("=" * 34)

over_limit_counts = 0
while True:
    label = input("label('quit' to stop):")
    label == "quit"
    break
value = float(input("value: "))
limit = float(input("limit:"))

difference, percent = check(value, limit)
status = status_of(percent)
if status == "OVER LIMIT":
    over_limit_counts += 1

print_report(label, value, limit, difference, percent, status)
print()
print(f"records over limit: {over_limit_counts}") 
