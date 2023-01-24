import tfce_types
import tfce_utils

def gen_state():
    for ore in tfce_types.ores:
        if ore[1]:
            
            # graded ores
            for grade in tfce_types.grades:
                for rock in tfce_types.rocks:
                    dir_path = "../src/main/resources/assets/tfc/blockstates/ore/" + grade + "_" + ore[0]
                    file_path =  dir_path + "/" + rock + ".json"
                    model_path = "tfc:block/ore/" + grade + "_" + ore[0] + "/" + rock
                    tfce_utils.create_simple_state(dir_path, file_path, model_path)
                
            # small ores
            dict = {}
            dir_path = "../src/main/resources/assets/tfc/blockstates/ore"
            file_path = dir_path + "/small_" + ore[0] + ".json"
            model_path = "tfc:block/groundcover/" + ore[0]
            tfce_utils.create_nested_dict(["variants", ""], [{}, {}, {}, {}], dict)
            dict["variants"][""][0] = {"model": model_path, "y": 90}
            dict["variants"][""][1] = {"model": model_path}
            dict["variants"][""][2] = {"model": model_path, "y": 180}
            dict["variants"][""][3] = {"model": model_path, "y": 270}
            tfce_utils.write_json(dict, file_path)


def gen_model():
    for ore in tfce_types.ores:
        if ore[1]:
            for grade in tfce_types.grades:
                for rock in tfce_types.rocks:
                    
                    # graded ores block
                    dict = {}
                    dir_path = "../src/main/resources/assets/tfc/models/block/ore/" + grade + "_" + ore[0]
                    file_path = dir_path + "/" + rock + ".json"
                    rock_path = "tfc:block/rock/raw/" + rock
                    overlay_path = "tfc:block/ore/" + grade + "_" + ore[0]
                    dict["parent"] = "tfc:block/ore"
                    dict["textures"] = {}
                    dict["textures"]["all"] = rock_path
                    dict["textures"]["particle"] = rock_path
                    dict["textures"]["overlay"] = overlay_path
                    tfce_utils.create_custom_block_model(dir_path, file_path, dict)
                    
                    # graded ores blockitem
                    dir_path = "../src/main/resources/assets/tfc/models/item/ore/" + grade + "_" + ore[0]
                    file_path = dir_path + "/" + rock + ".json"
                    parent_path = "tfc:block/ore/" + grade + "_" + ore[0] + "/" + rock
                    tfce_utils.create_simple_blockitem_model(dir_path, file_path, parent_path)
                    
                # graded ores item
                dir_path = "../src/main/resources/assets/tfc/models/item/ore"
                file_path = dir_path + "/" + grade + "_" + ore[0] + ".json"
                texture_path = "tfc:item/ore/" + grade + "_" + ore[0]
                tfce_utils.create_simple_item_model(dir_path, file_path, texture_path)
                
            # small ores item
            dir_path = "../src/main/resources/assets/tfc/models/item/ore"
            file_path = dir_path + "/small_" + ore[0] + ".json"
            texture_path = "tfc:item/ore/small_" + ore[0]
            tfce_utils.create_simple_item_model(dir_path, file_path, texture_path)
            

def gen_lang():
    
    file_path = "../src/main/resources/assets/tfcelem/lang/en_us.json"
    dict = tfce_utils.read_json(file_path)
    
    for ore in tfce_types.ores:
        if ore[1]:
            for grade in tfce_types.grades:
                for rock in tfce_types.rocks:
                    
                    trans_key = "block.tfc.ore." + grade + "_" + ore[0] + "." + rock
                    display_name = grade.title() + " " + rock.title() + " " + ore[0].replace("_", " ").title()
                    dict[trans_key] = display_name

                trans_key = "item.tfc.ore." + grade + "_" + ore[0]
                display_name = grade.title() + " " + ore[0].replace("_", " ").title()
                dict[trans_key] = display_name
            
            trans_key = "block.tfc.ore.small_"  + ore[0]
            display_name = "Small " + ore[0].replace("_", " ").title()
            dict[trans_key] = display_name
            
    tfce_utils.write_json(dict, file_path)


def register_tags():
    
    for ore in tfce_types.ores:
        if ore[1]:
            for grade in tfce_types.grades:

                values = []
                dir_path = "../src/main/resources/data/tfc/tags/blocks/ores/" + ore[0]
                file_path = dir_path + "/" + grade + ".json"
                for rock in tfce_types.rocks:
                    values.append("tfc:ore/" + grade + "_" + ore[0] + "/" + rock)
                tfce_utils.create_simple_tag(dir_path, file_path, values)