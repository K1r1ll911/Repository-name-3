# TODO решите задачу
import json

def task() -> float:
    with open("input.json", "r", encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)

    total_sum = 0.0

    for item in data:
        if 'score' in item and 'weight' in item:
            total_sum += item['score'] * item['weight']
    return round(total_sum, 3)

print(task())
