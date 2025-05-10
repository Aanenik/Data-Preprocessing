print(10)
import pandas as pd
from sklearn.preprocessing import StandardScaler # type: ignore
df=pd.read_csv("C:/Users/ANUJA NILAK/Downloads/DATAMITES DOCS/GIT & GITHUB/gitpractice/all_files/file.csv")
sc=StandardScaler()
df_final= sc.fit_transform(df)
print(df_final)
