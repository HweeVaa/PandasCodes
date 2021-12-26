import pandas as pd


list_data = ['2021-12-26',3.14,'ABC',100, True]
sr = pd.Series(list_data)
print(sr)

idx = sr.index
val = sr.values
print(idx)
print('\n')
print(val)
