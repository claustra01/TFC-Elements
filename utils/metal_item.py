import tfce_types
import tfce_utils

def create_metal_item_model(metal, types):
    for type in types:
        dir_path = "../src/main/resources/assets/tfc/models/item/metal/" + type
        file_path = dir_path + "/" + metal[0] + ".json"
        texture_path = "tfc:item/metal/" + type + "/" + metal[0]
        tfce_utils.create_simple_item_model(dir_path, file_path, texture_path)


def trans_metal_item(metal, types, dict) -> dict:
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


def gen_model():
    for metal in tfce_types.metals:
        
        # ingot
        dir_path = "../src/main/resources/assets/tfc/models/item/metal/ingot"
        file_path = dir_path + "/" + metal[0] + ".json"
        texture_path = "tfc:item/metal/ingot/" + metal[0]
        tfce_utils.create_simple_item_model(dir_path, file_path, texture_path)

        # tool
        if metal[1]:
            for type in tfce_types.types_tools:
                dict = {}
                dir_path = "../src/main/resources/assets/tfc/models/item/metal/" + type
                file_path = dir_path + "/" + metal[0] + ".json"
                colored_path = "tfc:item/metal/" + type + "/" + metal[0]
                handle_path = "tfc:item/metal/" + type + "/handle"
                tfce_utils.create_simple_item_model(dir_path, file_path, texture_path)
                dict["parent"] = "item/generated"
                tfce_utils.create_nested_dict(["textures", "layer0"], colored_path, dict)
                dict["textures"]["layer1"] = handle_path
                tfce_utils.create_dir(dir_path)
                tfce_utils.write_json(dict, file_path)

        # part
        if metal[2]:
            create_metal_item_model(metal, tfce_types.types_parts)

        # armor
        if metal[3]:
            create_metal_item_model(metal, tfce_types.types_armors)


def gen_lang():
    
    file_path = "../src/main/resources/assets/tfcelem/lang/en_us.json"
    dict = tfce_utils.read_json(file_path)

    for metal in tfce_types.metals:
        trans_key = "metal.tfc." + metal[0]
        display_name = metal[0].replace("_", " ").title()
        dict[trans_key] = display_name

        # ingot
        trans_key = "item.tfc.metal.ingot." + metal[0]
        display_name = metal[0].replace("_", " ").title() + " Ingot"
        dict[trans_key] = display_name
        
        # tool
        if metal[1]:
            trans_metal_item(metal, tfce_types.types_tools, dict)

        # part
        if metal[2]:
            trans_metal_item(metal, tfce_types.types_parts, dict)

        # armor
        if metal[3]:
            trans_metal_item(metal, tfce_types.types_armors, dict)

    tfce_utils.write_json(dict, file_path)


def gen_texture():
    return
