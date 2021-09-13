import pandas as pd
import helper_methods
import csv

def main():
    # The training set data frame
    df = pd.read_csv("titanic-data/train.csv")

    columns = ["PassengerId","Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"]

    survivors = df.loc[df['Survived'] == 1]

    percentage_survivors_from_total = len(survivors) / len(df)

    # Finds the most common values and their percentages from the list of survivors in the training set
    most_common_survivorship_values_for_features = helper_methods.scanSurvivorsForMostCommonFieldsAndSetPointValuesForThoseFields(survivors, columns)

    passengers_with_points_assigned = {}

    test_passenger_data_df = pd.read_csv("titanic-data/test.csv")
    test_passengers_with_points_assigned = {}

    # Gives each passenger in the test set a ranking value from their values
    for test_passenger in test_passenger_data_df.iterrows():
        test_passengers_with_points_assigned[test_passenger[1]["PassengerId"]] = helper_methods.assignSurvivalValueForPassenger(most_common_survivorship_values_for_features, test_passenger[1])

    # Sorting the test set allows us to pick the threshold index
    sorted_test_passengers_with_points = sorted(test_passengers_with_points_assigned, key=test_passengers_with_points_assigned.get, reverse=True)

    test_set_size = len(sorted_test_passengers_with_points)

    splitting_index = round(test_set_size * percentage_survivors_from_total)

    test_set_predicted_surviving_passengers = sorted_test_passengers_with_points[0:splitting_index]
    test_set_predicted_not_surviving_passengers = sorted_test_passengers_with_points[splitting_index: len(sorted_test_passengers_with_points)]

    total_set_test_data = []

    # Below we actually assign the survivorship and non survivorship values
    for row in test_set_predicted_not_surviving_passengers:
        total_set_test_data.append([row, 0])

    for row in test_set_predicted_surviving_passengers:
        total_set_test_data.append([row, 1])

    total_set_test_data_sorted_by_id = sorted(total_set_test_data)

    with open("results.csv", "w+") as csvfile:
        writer = csv.writer(csvfile)
        headers = ["PassengerId","Survived"]
        writer.writerow(headers)

        for row in total_set_test_data_sorted_by_id:
            writer.writerow(row)
    print('file results.csv has been created')

main()