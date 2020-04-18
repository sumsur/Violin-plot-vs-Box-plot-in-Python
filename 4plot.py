import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

#initialize a dataframe
asd = pd.read_excel(r'C:\Users\asd.xlsx', sheet_name='Sheet1')
asdd = pd.DataFrame(asd, columns= ['Mesec','Broj zahteva poslednjeg dana u mesecu'])


print('DataFrame\n----------\n', asdd)
print('\nDataFrame datatypes :\n', asdd.dtypes)

#convert pandas dataframe to numpy array
arr = asdd.to_numpy()


print('\nNumpy Array\n----------\n', arr)
print('\nNumpy Array Datatype :', arr.dtype)

plt.figure(1)
plot1=sns.violinplot(x='Mesec', y='Broj zahteva poslednjeg dana u mesecu', data=asdd)

plt.figure(2)
plot2=sns.boxplot(x='Mesec', y='Broj zahteva poslednjeg dana u mesecu', data=asdd)

plt.figure(3)
plot3=sns.swarmplot(x='Mesec', y='Broj zahteva poslednjeg dana u mesecu', data=asdd)

plt.figure(4)
plot4=sns.jointplot(x='Mesec', y='Broj zahteva poslednjeg dana u mesecu', data=asdd, kind='kde')
plt.show()