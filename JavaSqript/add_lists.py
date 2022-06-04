import json
numbers = 1213
filename = 'records.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
