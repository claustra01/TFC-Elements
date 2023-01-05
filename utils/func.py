import json

# Generate json
def gen_json(dict, file_path):
    f = open(file_path, "w")
    json.dump(dict, f, indent=2, ensure_ascii=False)
    f.close()

# Create nested dict
def create_nested_dict(list, val, dict, n=0):
    if n < len(list) - 1:
        dict[list[n]] = {}
        create_nested_dict(list, val, dict[list[n]], n + 1)
    else:
        dict[list[n]] = val
