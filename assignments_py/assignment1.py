# -*- coding: utf-8 -*-
"""Assignment1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bo2AfChzBRp85u4_h0R8zON9BPI-QW8t

#STQD6324
#assignment01
#P136922 PAN ZHANGYU

#diabetes.csv
# From： https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset
#Information about dataset attributes -

#Pregnancies: To express the Number of pregnancies

#Glucose: To express the Glucose level in blood

#BloodPressure: To express the Blood pressure measurement

#SkinThickness: To express the thickness of the skin

#Insulin: To express the Insulin level in blood

#BMI: To express the Body mass index

#DiabetesPedigreeFunction: To express the Diabetes percentage

#Age: To express the age

#Outcome: To express the final result 1 is Yes and 0 is No
"""

import pandas as pd

df = pd.read_csv('diabetes.csv')

print(df.head())

missing_values = df.isnull().sum()
print("Number of missing values:")
print(missing_values)


df_cleaned = df.dropna()

#  Alternatively, fill missing values ​​with the mean (或者，用平均值填充缺失值)
# df_cleaned = df.fillna(df.mean())

print("Data after processing missing values:")
print(df_cleaned.head())

mean = df_cleaned.mean()
std = df_cleaned.std()
lower_bound = mean - 2 * std
upper_bound = mean + 2 * std

outliers = (df_cleaned < lower_bound) | (df_cleaned > upper_bound)

outliers_rows = outliers.any(axis=1)

df_cleaned = df_cleaned[~outliers_rows]

print("Data after processing outliers:")
print(df_cleaned.head())

"""#This graph shows the distribution of glucose levels."""

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.hist(df_cleaned['Glucose'], bins=20, color='skyblue', edgecolor='black')

plt.title('Glucose Distribution')
plt.xlabel('Glucose')
plt.ylabel('Frequency')

plt.show()

"""#This figure shows that BIM data is mostly concentrated among young people, with most BIM levels ranging from 20 to 45."""

plt.figure(figsize=(10, 6))

plt.scatter(df_cleaned['Age'], df_cleaned['BMI'], color='green', alpha=0.5)

plt.title('BMI vs Age')
plt.xlabel('Age')
plt.ylabel('BMI')

plt.show()

"""#Outcome: To express the final result 1 is Yes and 0 is No
#It can be seen that patients with diabetes have higher glucose levels, and the values in the scattered points are higher.
"""

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

sns.scatterplot(data=df_cleaned, x='Glucose', y='Outcome', hue='Outcome', palette='Set1')

plt.title('Glucose vs Outcome')
plt.xlabel('Glucose')
plt.ylabel('Outcome')

plt.show()

"""#This is how to make a more intuitive picture.

"""

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.hist(df_cleaned[df_cleaned['Outcome'] == 1]['Glucose'], bins=20, color='skyblue', edgecolor='black', alpha=0.5, label='Outcome=1')

plt.hist(df_cleaned[df_cleaned['Outcome'] == 0]['Glucose'], bins=20, color='salmon', edgecolor='black', alpha=0.5, label='Outcome=0')

plt.title('Glucose Distribution by Outcome')
plt.xlabel('Glucose')
plt.ylabel('Frequency')
plt.legend()

plt.show()

"""#This graph shows that younger people have less diabetes than older people."""

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.hist(df_cleaned[df_cleaned['Outcome'] == 1]['Age'], bins=20, color='skyblue', edgecolor='black', alpha=0.5, label='Outcome=1')

plt.hist(df_cleaned[df_cleaned['Outcome'] == 0]['Age'], bins=20, color='salmon', edgecolor='black', alpha=0.5, label='Outcome=0')

plt.title('Age Distribution by Outcome')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend()

plt.show()