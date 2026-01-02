## question 1
data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [18, 19, 20, 21],
    'Marks': [80, None, 90, None]
}

# find mean
mean(): average_age = df['Age'].mean()
# delete Age column
drop(): df.drop("Age",axis=1)
# fill mean value in null space
fillna(): df['Age'] = df['Age'].fillna(df['Age'].mean())

## question 2 
data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [18, 19, 20, 21],
    'Marks': [80, None, 90, None]
}

# change from DataFram to ndarray
df.to_numpy()
# turn the matrix 90 degree
np.rot90(): np.rot90(array)
# print the oldest person's name
np.argmax(): df.loc[np.argmax(df['Age']), 'Name']

## question 3

import numpy as np
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
data1 = [3, 7, 5, 2]
data2 = [4, 6, 3, 8]

x = np.arange(len(categories))
bar_width = 0.4

plt.bar(x - bar_width / 2, data1, width = bar_width, label = 'Dataset 1', color = 'royalblue')
plt.bar(x + bar_width / 2, data2, width = bar_width, label = 'Dataset 2', color = 'darkorange')
plt.xticks(x, categories)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.legend()
plt.show()

## question 4

# filter students with Math score over average
import pandas as pd
df = pd.read_csv("student_scores.csv")
mean = df['Math'].mean()
print(df[df['Math'] >= mean])

# Create new Status column, where if the student to >60 on average they pass, else failed
df['Average_Score'] = df[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean(axis = 1)
df['Status'] = df['Average_Score'].apply(lambda x: 'Pass' if x > 60 else 'Fail')
df.drop('Average_Score', axis = 1, inplace = True)
print(df)
