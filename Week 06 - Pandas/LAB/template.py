"""
RECORD CHECK  -  my version
===========================

Name  :Ismail joma
Lane  : IT
Date  :13/11/26

Run it:   Mini_project_06.py

"""
import pandas as pd

df = pd.read_csv("servers.csv")
df["percent"] = (df["used_gb"] / df["total_gb"]) * 100
print(df)


df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

print(df[df["status"] != "OK"])