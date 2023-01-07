import func

# Generate basic blockitem model
def gen_blockitem(parent_path, file_path):
    dict = {}
    dict["parent"] = parent_path
    func.gen_json(dict, file_path)

# Generate basic item model
def gen_item(texture_path, file_path):
    dict = {}
    dict["parent"] = "item/generated"
    func.gen_nested_dict(["textures", "layer0"], texture_path, dict)
    func.gen_json(dict, file_path)

# Generate metal item model
def gen_metal_item(types, metal):
    for type in types:
        texture_path = "tfc:item/metal/" + type + "/" + metal[0]
        file_path = "../src/main/resources/assets/tfc/models/item/metal/" + type + "/" + metal[0] + ".json"
        gen_item(texture_path, file_path)
