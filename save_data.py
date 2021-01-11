import json


def save_json(data, filename):
    # Save data to JSON file
    file_path = "./data/" + filename + ".json"
    with open(file_path, mode="w") as file:
        json.dump(data, fp=file)
