import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files

uploaded = files.upload()

import os
print(os.listdir())

# read file + show basic info
X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')
X_pred = pd.read_csv('X_private_test.csv')

X_train.shape, y_train.shape, X_pred.shape

# house price distribution visualisation
price = df['price']

q1 = price.quantile(0.25)
q3 = price.quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

outliers = df[(price <= lower_bound) | (price >= upper_bound)]
common_data = df[(price > lower_bound) & (price < upper_bound)]

plt.figure(figsize=(10, 6))
plt.hist(common_data['price']/1000, bins=50, color='blue', edgecolor='black', label="Common house price values")
plt.scatter(outliers['price']/1000, np.zeros_like(outliers['price']), color='red', label="Ourliers house price values", zorder=5)

plt.axvline(lower_bound/1000, color='purple', linestyle='--', label="Lower bound")
plt.axvline(upper_bound/1000, color='purple', linestyle='--', label="Upper bound")

plt.title("House price distribution frequency")
plt.xlabel("Price (thousand $)")
plt.ylabel("Frequency")
plt.legend(loc='upper right')
plt.show()

# living area distribution visualization
living_area = df['sqft_living'].to_numpy()

lower_bound = np.percentile(living_area, 10)
upper_bound = np.percentile(living_area, 90)

outliers = df[(df['sqft_living'] <= lower_bound) | (df['sqft_living'] >= upper_bound)]
common_data = df[(df['sqft_living'] > lower_bound) | (df['sqft_living'] < upper_bound)]

plt.figure(figsize=(10, 6))
plt.hist(common_data['sqft_living'], bins=50, color='blue', edgecolor='black', label="Common area of living")
plt.scatter(outliers['sqft_living'], np.zeros_like(outliers['sqft_living']), color='red', label="Ourliers area of living", zorder=5)

plt.axvline(lower_bound, color='purple', linestyle='--', label="Lower bound")
plt.axvline(upper_bound, color='purple', linestyle='--', label="Upper bound")

plt.title("Living area distribution frequency")
plt.xlabel("Area (square ft)")
plt.ylabel("Frequency")
plt.legend(loc='upper right')
plt.show()

# bedroom distribution visualization
bedroom = df['bedrooms']

q1 = bedroom.quantile(0.25)
q3 = bedroom.quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df[(bedroom< lower_bound) | (bedroom >upper_bound)]
common_data = df[(bedroom >= lower_bound) | (bedroom<= upper_bound)]

plt.figure(figsize=(10, 6))
plt.hist(common_data['bedrooms'], bins=50, color='blue', edgecolor='black', label="Common number of bedroom")
plt.scatter(outliers['bedrooms'], np.zeros_like(outliers['bedrooms']), color='red', label="Ourliers number of bedroom", zorder=5)

plt.axvline(lower_bound, color='purple', linestyle='--', label="Lower bound")
plt.axvline(upper_bound, color='purple', linestyle='--', label="Upper bound")

plt.title("Number of bedroom distribution frequency")
plt.xlabel("bedroom")
plt.ylabel("Frequency")
plt.legend(loc='upper right')
plt.show()

# correlation heatmap
number_value = df.select_dtypes(include=['float64','int64'])

plt.figure(figsize=(12,10))
sns.heatmap(number_value.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.8)

plt.title('Heat map for all categories')
plt.show()

# condition distribution visualization
house_condition = df.groupby('condition').size()

house_condition.plot(kind='bar', figsize=(10,8))
plt.title('Distribution of condition')
plt.xlabel('Condition')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.show()

# year built distribution visualization
df['year_interval'] = (df['yr_built']//10)*10
year_built = df.groupby('year_interval').size()

year_built.plot(kind='bar', figsize=(10,8))
plt.title('Distribution of year built')
plt.xlabel('Year built')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.show()

# missing value
X_train_null = X_train.columns[X_train.isnull().any()]
for col in X_train_null:
    print(f"{col} with {X_train[col].isnull().sum()/len(X_train[col]) * 100}")

X_train['f2'].fillna(X_train['f2'].median(), inplace=True)
X_train['f5'].fillna(X_train['f5'].median(), inplace=True)
X_train['f10'].fillna(X_train['f10'].median(), inplace=True)

# feature importance
from xgboost import XGBClassifier

model = XGBClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

feature_importance = model.feature_importances_
importance_df = pd.DataFrame({"Feature": X_train.columns, "Importance": feature_importance}).sort_values(by="Importance", ascending=False)
importance_df

# feature selection

from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import SelectKBest

mi_scores = mutual_info_classif(X_train, y_train)

k_best = SelectKBest(mutual_info_classif, k=3)
X_selected = k_best.fit_transform(X_train, y_train)
print(X_selected)
selected_mi = pd.DataFrame({'Feature': X_train.columns, 'Mutual Information': mi_scores})
selected_mi = selected_mi.sort_values(by='Mutual Information', ascending=False)
selected_mi

# split train test
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

X_train, X_val, y_train, y_val = train_test_split(X_train_pca, y_train, test_size=0.2, random_state=42)

model = XGBClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_val)
f1 = f1_score(y_val, y_pred,average='macro')
print(f"F1 Score: {f1}")
