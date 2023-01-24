import tfce_types
import tfce_utils

def register_tags():
    
    # ore pieces
    values = []
    dir_path = "../src/main/resources/data/tfc/tags/items"
    file_path = dir_path + "/ore_pieces.json"
    for ore in tfce_types.ores:
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
