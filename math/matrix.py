import pandas as pd
import numpy as np

selected_items = df.loc[item_names]
stat_columns = list(constraints.keys())
item_stats = selected_items[stat_columns]
A = item_stats.T.to_numpy(dtype=float)
b = np.array(list(constraints.values()), dtype=float)

rows, cols = A.shape
determinant = np.linalg.det(A) if rows == cols else 0
