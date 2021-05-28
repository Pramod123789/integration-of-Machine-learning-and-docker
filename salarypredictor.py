import pandas
ds = pandas.read_csv('SalaryData.csv')
x = ds['YearsExperience'].values.reshape(30,1)
y = ds['Salary']
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x , y)
d=int(input("enter your experience in number of years "))
n=model.predict([[ d ]] )
print(f'The comopany can offer you salary Rs  {n} ')
