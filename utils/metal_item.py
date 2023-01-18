import tfce_types
import tfce_utils

def create_metal_item_model(metal, types):
    for type in types:
        dir_path = "../src/main/resources/assets/tfc/models/item/metal/" + type
        file_path = dir_path + "/" + metal[0] + ".json"
        texture_path = "tfc:item/metal/" + type + "/" + metal[0]
        tfce_utils.create_simple_item_model(dir_path, file_path, texture_path)


def gen_model():
    for metal in tfce_types.metals:
        
        # ingot item model
        dir_path = "../src/main/resources/assets/tfc/models/item/metal/ingot"
        file_path = dir_path + "/" + metal[0] + ".json"
        texture_path = "tfc:item/metal/ingot/" + metal[0]
        tfce_utils.create_simple_item_model(dir_path, file_path, texture_path)

        # tool item model
        if metal[1]:
            create_metal_item_model(metal, tfce_types.types_tools)

        # part item model
        if metal[2]:
            create_metal_item_model(metal, tfce_types.types_parts)

        # armor item model
        if metal[3]:
            create_metal_item_model(metal, tfce_types.types_armors)


def gen_lang():
    return


def gen_texture():
    return
