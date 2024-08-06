import numpy as np
import pandas as pd


# importing csv files
df = pd.read_csv("diabetes.csv")

# You can do the same to import TXT files: 
df = pd.read_csv('diabetes.txt', sep="\s")

# And the same for excel sheets (single sheet):
df = pd.read_excel('diabetes.xlsx')

# Multiple excel sheets:
df = pd.read_excel('diabetes_multi.xlsx', sheet_name=1)  # REMINDER: python usses 0-indexing

# Importing a JSON file: 
df = pd.read_json('diabetes.json')

# NOTE: Panda allows you to Output the data into the same types that you can import from

# Outputting into CSV: 
df.to_csv('diabetes_out.csv', index=False)  
# index=False argument specifies that the index column should not be included in the output file

# And its the same with all the other ones just the syntax might change at times :
df.to_json('diabetes_out.json')
df.to_excel('diabetes_out.xlsx', index=False)
df.to_csv('diabetes_out.txt', header=df.columns, index=None, sep= ' ')

# NOTE: You can use "head()" and "tail()" to view the first and last rows of a Dataframe
df.head(n=3) 
df.tail(n=10) # last 10 rows of the Dataframe

# Using .describe(): prints the summary of statistics of all numeric columns. 

df.describe(percentiles=[0.4, 0.5, 0.7])
df.describe(include=[int]) #include is used to specify the data types 
df.describe(exclude=[int])
df.describe().T # T: makes the rows, columns and vise versa 

# info: quick way to look at data types, missing values, and datasize of dataframes 
# show_counts is set to true so gives a few over the total non-missing values in each column. 
# memory_usage is set to true which shows the total memory usage of the dataframe elemets. 
# verbose is set to true to print the full summary from .info()

df.info(show_counts=True, memory_usage=True, verbose=False)

# Understanding data using .shape, it returns a tuple and can be indexed to get only rows, and only columns as an output
df.shape # gets the number of rows and columns
df.shape[0] # number of rows only
df.shape[1] # number of columns

# Get all Columns and Column names 
df.columns 
# it can be converted to a list using list() function 
list(df.columns)

# to check missing values we use .isnull()
df2 = df.copy()
df2.loc[2:5, 'Pregnancies'] = None
df2.head(7)
# ---------
df2.isnull().head(7)
df2.isnull().sum() # to count the number of missing data in each column
df2.isnull().sum().sum() # to count the number of nulls in the whole data frame 

# To isolate a signle column []
df['outcome']

# isolating two or more columns [[]]
df[['Pregnancies', 'outcome']]

# isolating one row using []
df[df.index == 1]

# two or more rows using []
df[df.index.isin(range(2,10))]

# Using .loc[] and .iloc[] to fetch rows ("location" and "integer location")
df2.index = range(1,769)
df2.loc[1]
df2.iloc[1]
df2.loc[100:110]
df2.iloc[100:110]
df2.loc[[100, 200, 300]]
df2.loc[100:110, ['Pregnancies', 'Glucose', 'BloodPressure']]
df2.loc[df['Age']==81, ['Age']] = 80


# NOTE: Dealing with missing data technique 
# 1: Dropping missing values
df3 = df2.copy()
df3 = df3.dropna()
df3.shape

#2: Replacing missing values
df3 = df2.copy()
# Get the mean of Pregnancies
mean_value = df3['Pregnancies'].mean()
# Fill missing values using .fillna()
df3 = df3.fillna(mean_value)

# NOTE: Dealing with Duplicate Data
df3 = pd.concat([df2, df2])
df3.shape

df3 = df3.drop_duplicates()
df3.shape

# Renaming columns
df3.rename(columns = {'DiabetesPedigreeFunction':'DPF'}, inplace = True)
df3.head()

df3.columns = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DPF', 'Age', 'Outcome', 'STF']
df3.head()

# NOTE: Data analysis in pandas
df.mean()
df.mode()
df.median()

# Create new columns based on existing columns 
df2['Glucose_Insulin_Ratio'] = df2['Glucose']/df2['Insulin']
df2.head()

# Counting using .value_counts()
df['Outcome'].value_counts()
df['Outcome'].value_counts(normalize=True)
df['Outcome'].value_counts(sort=False)
df.value_counts(subset=['Pregnancies', 'Outcome'])

# Aggregating data with .groupby() in pandas
df.groupby('Outcome').mean()
df.groupby(['Pregnancies', 'Outcome']).mean()

# Pivot tables 
pd.pivot_table(df, values="BMI", index='Pregnancies', 
               columns=['Outcome'], aggfunc=np.mean)

# Line plots in pandas
df[['BMI', 'Glucose']].plot.line()
df[['BMI', 'Glucose']].plot.line(figsize=(20, 10), 
                                 color={"BMI": "red", "Glucose": "blue"})
df[['BMI', 'Glucose']].plot.line(figsize=(20, 10), 
                                 color={"BMI": "red", "Glucose": "blue"})

# Bar plots in pandas
df['Outcome'].value_counts().plot.bar()
df.boxplot(column=['BMI'], by='Outcome')