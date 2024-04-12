# How to Split a Pandas DataFrame into Chunks

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'experience': [1, 1, 5, 7, 7, 10],
    'salary': [175.1, 180.2, 190.3, 205.4, 210.5, 225.3],
})


list_of_dataframes = np.array_split(df, 2)
print(list_of_dataframes)