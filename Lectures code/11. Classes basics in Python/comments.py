def convert_list_to_dict(persons_list):
    mapping = {"name": 0,
               "age": 1}

    result = []
    for person in persons_list:
        person_as_dict = dict()
        person_as_dict["name"] = person[mapping["name"]]
        person_as_dict["age"] = person[mapping["age"]]
        result.append(person_as_dict)
    return result


lst = [["John", 32], ["Ann", 18]]

print(convert_list_to_dict(lst))