def scanSurvivorsForMostCommonFieldsAndSetPointValuesForThoseFields(survivors, columns):
    most_common_map = {}

    for feature in columns:
        most_common_map[feature] = survivors.value_counts(feature, normalize=True)
    return most_common_map

def assignSurvivalValueForPassenger(most_common_map, passenger):
    passenger_sum = 0

    for feature in passenger.keys():
        if passenger[feature] and passenger[feature] in most_common_map[feature]:
            passenger_sum += most_common_map[feature][passenger[feature]]
    return passenger_sum