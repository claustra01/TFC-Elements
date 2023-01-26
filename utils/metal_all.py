import tfce_types
import tfce_utils

def register_tags():

    # ingots
    values = []
    for metal in tfce_types.metals:
        values.append("tfc:metal/ingot/" + metal[0])
    dir_path = "../src/main/resources/data/forge/tags/items"
    tfce_utils.create_simple_tag(dir_path, dir_path + "/ingots.json", values)
    dir_path = "../src/main/resources/data/tfc/tags/items"
    tfce_utils.create_simple_tag(dir_path, dir_path + "/pileable_ingots.json", values)
    
    # parts
    if metal[2]:
        for type in tfce_types.types_parts:
            values = []
            for metal in tfce_types.metals:
                values.append("tfc:metal/" + type + "/" + metal[0])
            dir_path = "../src/main/resources/data/forge/tags/items"
            tfce_utils.create_simple_tag(dir_path, dir_path + "/" + type + "s.json", values)
            if type == "sheet":
                dir_path = "../src/main/resources/data/tfc/tags/items"
                tfce_utils.create_simple_tag(dir_path, dir_path + "/pileable_sheets.json", values)
