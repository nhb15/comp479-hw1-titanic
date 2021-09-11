import numpy as np
import pandas as pd
import helper_methods

df = pd.read_csv("titanic-data/train.csv")

# going to try a fun way similar to the one from class by taking the percentage of people who survived the crash
columns = ["PassengerId","Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"]

gradeable_columns = ["Pclass","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"]

survivors = df.loc[df['Survived'] == 1]
feature_map = {}

most_common_survivorship_values_for_features = helper_methods.scanSurvivorsForMostCommonFieldsAndSetPointValuesForThoseFields(survivors, gradeable_columns)

survivorship_points_for_most_common_features = helper_methods.convertCountsIntoPointValues(most_common_survivorship_values_for_features)

percentage_survivors_from_total = round((len(survivors) / len(df)) * 100)
print(percentage_survivors_from_total)
#IDEAS
"""
Find the most common feature values of survivors. Then, rank the test set based on the number of values matched and rate top tier matches more
This approach works on predicting groups of test sets rather than individual rows. If we wanted the ability to predict individual rows, we could find the threshold value
of our percentage_survivors_from_total and see if the prediced value is above or below.


Gender could play a role
Age definitely plays a role
Parents and siblings could play a role for kids
cabin number could play a role for boat positioning
"""


# columns_weight_map = {
#     "PassengerId": 0,
#     "Survived": 0,
#     "Pclass": 0,
#     "Name": 0,
#     "Sex": 0,
#     "Age": 0,
#     "SibSp": 0,
#     "Parch": 0,
#     "Ticket": 0,
#     "Fare": 0,
#     "Cabin": 0,
#     "Embarked": 0
# }