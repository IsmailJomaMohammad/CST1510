import pandas as pd

app_sizes = pd.Series([45,120,15], index= ["Photos","Games","Music"])

phones = pd.DataFrame({

    "model": ["Phone A","Phone B","Phone C" ],
    "total_storage_gb": [128,256,64],
    "used_storage_gb": ["96","128","50"]

})

phones["used_storage_gb"] = phones["used_storage_gb"].astype(int)
phones["free_storage_gb"] = phones["total_storage_gb"] - phones["used_storage_gb"]
phones["percent_used"] = phones["used_storage_gb"]/phones["total_storage_gb"] * 100

print(phones)