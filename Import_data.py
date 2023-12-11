import pandas as pd
import os
path = "C:\Coding_python\Data\motion-and-heart-rate-from-a-wrist-worn-wearable-and-labeled-sleep-from-polysomnography-1.0.0\heart_rate"
dir_list = os.listdir(path)
print("Files and Directories in '", path, "' :")
print(dir_list)
df = pd.read_csv(path + '\\' + dir_list[0])
print(df)