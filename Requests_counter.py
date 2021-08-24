import pandas as pd
from matplotlib import pyplot as plt

requests_test_data = pd.read_csv('C:\\Users\\Anzhaner\\Desktop\\Python\\MyTest\\TestData\\requests_test.csv')

df = requests_test_data.copy()

df['month_year'] = df['Время. Создание заявки'].map(lambda x: str(x)[6:11] + str(x)[3:5])
resultdf=df.groupby("month_year").agg({'Время. Создание заявки': 'count', 'ФИО': 'count'}).rename(columns={"month_year":"Count"})

resultdf = pd.DataFrame(resultdf)
resultdf['Counter'] = resultdf['Время. Создание заявки']
print(resultdf['Counter'])

plt.plot(resultdf.index, resultdf['Counter'], color='blue', marker='o')
plt.grid()
plt.xlabel('Дата')
plt.ylabel('Количество заявок')
plt.xticks(rotation=90)
plt.show()
