import pandas as pd

data=pd.read_csv('bmi_data.csv')

print(data)
group=data.groupby('Gender')
c=group.describe()
print(c)


