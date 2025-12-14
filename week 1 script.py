# Intro to Python
# Week1
# 311246169 Noa Beiman

import pandas as pd
data = {"subject_number":[1,2,3,4,5,6], "age":[15,16,17,18,19,20], "gender":["m","f","m","f","m","f"], "depression":[1,0,1,0,1,0], "anxiery": [1,1,1,0,1,1]}
df = pd.DataFrame(data)
df.to_csv("data.csv")
