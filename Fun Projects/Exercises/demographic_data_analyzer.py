"""
In this challenge you must analyze demographic data using Pandas. 
You are given a dataset of demographic data that was extracted from 
the 1994 Census database.
http://archive.ics.uci.edu/ml/index.php


You must use Pandas to answer the following questions:

1 - How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
2 - What is the average age of men?
3 - What is the percentage of people who have a Bachelor's degree?
4 - What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
5 - What percentage of people without advanced education make more than 50K?
6 - What is the minimum number of hours a person works per week?
7 - What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
8 - What country has the highest percentage of people that earn >50K and what is that percentage?
9 - Identify the most popular occupation for those who earn >50K in India.

Use the starter code in the file demographic_data_analyzer. Update the code so 
all variables set to "None" are set to the appropriate calculation or code. 
Round all decimals to the nearest tenth.

References:
https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer
"""


import pandas as pd
import numpy as np

# importing data:
col_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num',
            'marital_status', 'occupation', 'relationship', 'race',
            'sex', 'capital-gain', 'capital-loss', 'hours-per-week',
            'native-country', 'salary']
dati = pd.read_csv(r'C:\Users\rbuzzini\Documents\Personale\Git\Python\Fun Projects\datasets\adult.data',
                   header=0,
                   names=col_names)

# df overview:
dati.shape
dati.info()
dati.head()

# 1 - How many people of each race are represented in this dataset? 
# This should be a Pandas series with race names as the index labels. (race column)
dati['race'].value_counts().sort_values(ascending=False)

# 2 - What is the average age of men?
dati['sex'] = dati['sex'].str.strip()   # removing leading and ending white spaces
avg_men_age = round(dati.loc[dati['sex'] == 'Male', 'age'].mean(), 1)
avg_men_age

# 3 - What is the percentage of people who have a Bachelor's degree?
dati['education'] = dati['education'].str.strip()
bachelors_percentage = '{:.1%}'.format(dati['education'].value_counts(normalize=True)['Bachelors'])
bachelors_percentage

# 4 - What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
dati['salary'] = dati['salary'].str.strip()
advanced_education = dati[dati['education'].isin(
    ['Bachelors', 'Masters', 'Doctorate']
    )]

high_education_salary_percentage = '{:.1%}'.format(advanced_education['salary'].value_counts(normalize=True)['>50K'])
high_education_salary_percentage

# 5 - What percentage of people without advanced education make more than 50K?
poor_education = dati[~dati.index.isin(advanced_education.index)]
poor_education_high_salary_percentage = '{:.1%}'.format(poor_education['salary'].value_counts(normalize=True)['>50K'])
poor_education_high_salary_percentage


# 6 - What is the minimum number of hours a person works per week?
min_hours_per_week = dati['hours-per-week'].min()
min_hours_per_week

# 7 - What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
high_salary_working_less_percentage = '{:.1%}'.format(
    dati.loc[dati['hours-per-week'] == min_hours_per_week, 'salary']
        .value_counts(normalize=True)['>50K']
    )
high_salary_working_less_percentage

# 8 - What country has the highest percentage of people that earn >50K and what is that percentage?
dati['native-country'] = dati['native-country'].str.strip()
high_salary_percentage_per_country = dati.groupby(['native-country', 'salary'])['salary'].count() / dati.groupby(['native-country'])['native-country'].count()
        #.reset_index())
high_salary_percentage_per_country[:, '>50K'].sort_values(ascending=False).index[0]

# 9 - Identify the most popular occupation for those who earn >50K in India.
dati['occupation'] = dati['occupation'].str.strip()
dati.loc[dati['native-country'] == 'India', 'occupation'].value_counts(ascending=False).index[0]