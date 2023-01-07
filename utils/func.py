import json

# Generate json
def gen_json(dict, file_path):
    f = open(file_path, "w")
    json.dump(dict, f, indent=2, ensure_ascii=False)
    f.close()

# Create nested dict
def gen_nested_dict(list, val, dict, n=0):
    if n < len(list) - 1:
        dict[list[n]] = {}
        gen_nested_dict(list, val, dict[list[n]], n + 1)
    else:
        dict[list[n]] = val

# Generate basic blockitem model
def gen_blockitem(parent_path, file_path):
    dict = {}
    dict["parent"] = parent_path
    gen_json(dict, file_path)

# Generate basic item model
def gen_item(texture_path, file_path):
    dict = {}
    dict["parent"] = "item/generated"
    gen_nested_dict(["textures", "layer0"], texture_path, dict)
    gen_json(dict, file_path)

# Generate metal item model
def gen_metal_item(types, metal):
    for type in types:
        texture_path = "tfc:item/metal/" + type + "/" + metal[0]
        file_path = "../src/main/resources/assets/tfc/models/item/metal/" + type + "/" + metal[0] + ".json"
        gen_item(texture_path, file_path)

# Generate metal item lang key
def trans_metal_item(types, metal, dict) -> dict:
    for type in types:
        trans_key = "item.tfc.metal." + type + "." + metal[0]
        if type == "propick":
            display_name = metal[0].replace("_", " ").title() + " " + "Prospector's Pick"
        elif type == "propick_head":
            display_name = metal[0].replace("_", " ").title() + " " + "Prospector's Pick Head"
        else:
            display_name = metal[0].replace("_", " ").title() + " " + type.replace("_", " ").title()
        dict[trans_key] = display_name
    return dict
