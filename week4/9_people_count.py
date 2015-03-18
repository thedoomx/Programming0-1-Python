def get_people_count(activity):
    result = {}

    for person in activity:
        if person in result:
            result[person] += 1
        else:
            result[person] = 1

    return len(result)
