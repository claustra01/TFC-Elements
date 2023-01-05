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

# Generate metal item model
def gen_metal_item(types, metal):
    for type in types:
        dict = {}
        texture_path = "tfc:item/metal/" + type + "/" + metal[0]
        file_path = "../src/main/resources/assets/tfc/models/item/metal/" + type + "/" + metal[0] + ".json"
        dict["parent"] = "item/generated"
        create_nested_dict(["textures", "layer0"], texture_path, dict)
        gen_json(dict, file_path)
