import math

def scanSurvivorsForMostCommonFieldsAndSetPointValuesForThoseFields(survivors, columns):
    most_common_map = {}
    set_of_three_point_values = [10, 5, 2]

    for feature in columns:
        most_common_map[feature] = survivors.value_counts(feature).head(3)
        index = 0
        for common_count in most_common_map[feature]:
            print(common_count)
            print(index)
            index += 1
    return most_common_map

def convertCountsIntoPointValues(most_common_map):
    print(most_common_map)

def assignSurvivalValueForPassenger(most_common_map, passenger):
    print(passenger)

# def findSurvivalPercentageOfTrainData(test_data):
#     print(test_data)

# def designateTrainDataAndTestDataFromSource(source_data, percentage_train):
#     # Assume the data is not organized in any way
#     data_set_size = len(source_data['PassengerId'])
#     splitting_index = round((percentage_train / 100) * data_set_size)
#
#     training_data = source_data.iloc[0:splitting_index]
#     test_data = source_data.iloc[(splitting_index+1):110]
#
#     print(training_data)
#     return training_data, test_data