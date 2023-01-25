import tfce_types
import tfce_utils

def register_tags():
    
    # ore blocks
    values = []
    for ore in tfce_types.ores:
        if ore[1]:
            for grade in tfce_types.grades:
                values.append("#tfc:ores/" + ore[2] + "/" + grade)
    dir_path = "../src/main/resources/data/minecraft/tags/blocks/mineable"
    tfce_utils.create_simple_tag(dir_path, dir_path + "/pickaxe.json", values)
    dir_path = "../src/main/resources/data/forge/tags/blocks"
    tfce_utils.create_simple_tag(dir_path, dir_path + "/ores.json", values)
    dir_path = "../src/main/resources/data/tfc/tags/blocks"
    tfce_utils.create_simple_tag(dir_path, dir_path + "/can_trigger_collapse.json", values)
    tfce_utils.create_simple_tag(dir_path, dir_path + "/monster_spawns_on.json", values)
    tfce_utils.create_simple_tag(dir_path, dir_path + "/can_collapse.json", values)
    tfce_utils.create_simple_tag(dir_path, dir_path + "/prospectable.json", values)
    tfce_utils.create_simple_tag(dir_path, dir_path + "/can_start_collapse.json", values)
    dir_path = "../src/main/resources/data/tfc/tags/blocks/rock"
    tfce_utils.create_simple_tag(dir_path, dir_path + "/ores.json", values)
        
    # register ore block hardness
    for ore in tfce_types.ores:
        if ore[3] == "stone":
            dir_path = "../src/main/resources/data/minecraft/tags/blocks"
            file_path = dir_path + "/needs_stone_tool.json"
        elif ore[3] == "iron":
            dir_path = "../src/main/resources/data/minecraft/tags/blocks"
            file_path = dir_path + "/needs_iron_tool.json"
        elif ore[3] == "diamond":
            dir_path = "../src/main/resources/data/minecraft/tags/blocks"
            file_path = dir_path + "/needs_diamond_tool.json"
        elif ore[3] == "netherite":
            dir_path = "../src/main/resources/data/forge/tags/blocks"
            file_path = dir_path + "/needs_netherite_tool.json"
        else:
            continue
        if ore[1]:
            for grade in tfce_types.grades:
                dict = tfce_utils.read_json(file_path)
                values = dict["values"]
                values.append("#tfc:ores/" + ore[2] + "/" + grade)
                dict["values"] = values
                tfce_utils.write_json(dict, file_path)
    
    # ore pieces
    values = []
    dir_path = "../src/main/resources/data/tfc/tags/items"
    file_path = dir_path + "/ore_pieces.json"
    for ore in tfce_types.ores:
        if ore[1]:
            for grade in tfce_types.grades:
                values.append("tfc:ore/" + grade + "_" + ore[0])
    tfce_utils.create_simple_tag(dir_path, file_path, values)
    
    # small ores
    values = []
    dir_path = "../src/main/resources/data/tfc/tags/items"
    for ore in tfce_types.ores:
        values.append("tfc:ore/small_" + ore[0])
    tfce_utils.create_simple_tag(dir_path, dir_path + "/small_ore_pieces.json", values)
    tfce_utils.create_simple_tag(dir_path, dir_path + "/nuggets.json", values)
