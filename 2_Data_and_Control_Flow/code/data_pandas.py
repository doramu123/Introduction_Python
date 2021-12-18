# add row sum
# add column sum
# unique


# Pandas
import pandas as pd

# Pandas read examples:
# https://www.datacamp.com/community/tutorials/importing-data-into-pandas

# be careful with backward slash \

import os
os.getcwd()  
os.chdir(r'2_Data_and_Control_Flow\code')

df = pd.read_excel(r"..\data\data.xlsx")

df.info()
df.dtypes
df.head() # first 
df.tail() # last # df.tail(3)

df.describe() # descriptive statis

df.columns
df.index
df['age']
df['firstName']



# iloc
df.iloc[2,1]
df.iloc[2:5,1:3]

# loc - index
df.loc[5,"lastName"]
df.loc[5:8,"lastName"]
df.loc[5:8,("lastName","firstName")]

df.set_index('firstName',drop=False, inplace=True) # , 
df.loc["Gerel","lastName"]


# filter
df[df["age"]<27]
df[~(df['age']<27)]['age']
df[df["age"]<27][["firstName","lastName","salary","age"]]
df[df["age"]>=27][["firstName","lastName","salary","age"]]


df[(df["age"]<27) & (df["salary"]<2.0) & (df["gender"] != "M")]
df[(df["age"]<27) & (df["salary"]<2.0) & (df["gender"] == "F")]

df.groupby('gender')['salary'].mean()
df.groupby("gender")['salary'].max()
df.groupby("gender")['salary'].min()

df.groupby(['gender','politicalView'])['age'].mean()


df.groupby(['gender','politicalView'])['age'].mean()
df.groupby(['gender','politicalView'])[['age','salary']].mean()
df.groupby(['gender','politicalView'])[['age','salary']].max()

# df.groupby('A').agg({'B': ['min', 'max'], 'C': 'sum'})
res = df.groupby(['gender','politicalView']) \
        .agg({'age': ["mean","max"], 'salary': ["max","count"]})
len(res.columns)
res[('age','mean')]
res['age']


df = df.sort_values(by="yearsInCompany", ascending=False)

df.sort_values(by="gender", inplace=True)
df["name"] = np.arange(10)
del df["name"]

df.reset_index(drop=True,inplace=True)

df[["age","salary"]]

# statistics and values
df['age'].mean()
df['age'].sum()
df['age'].max()
df['age'].min()
df['gender'].unique() # array with unique elements
df.values


# type conversion
data = {'Salary':[1000, 2222, 3321, 4414, 5151],
       'Name': ['Pete', 'Steve',
                   'Brian',
                   'Ryan', 'Jim'],
       'Share':[29.88, 19.05, 8.17,
               7.3, 6.15],
       'Date':['11/24/2020', '12/21/2019', 
               '10/14/2018', '12/13/2017', '01/08/2017'],
       'Date2': [20120902, 20130413, 20140921, 20140321,
                20140321]}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.info()
df['Date2'] = pd.to_datetime(df['Date2'])
df['Date'] = df['Date'].astype('datetime64[ns]')


# saving to files
df.to_csv('../result/my.csv')
df.to_json('../result/my.json')
df.to_excel('../result/my.xlsx')