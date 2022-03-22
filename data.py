import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport


df = pd.read_excel('teste.xlsx')



profile = ProfileReport(df, title="Pandas Profiling Report")
print(profile)