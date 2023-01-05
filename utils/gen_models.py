import namelist
import func

# Generate ore model files
def ore_model_gen():
    for ore in namelist.ores:
        
        # Graded ores
        if ore[1]:
            for grade in namelist.grades:
                for rock in namelist.rocks:
                    
                    # Ore block models
                    dict = {}
                    rock_path = "tfc:block/rock/raw/" + rock
                    overlay_path = "tfc:block/ore/" + grade + "_" + ore[0]
                    file_path = "../src/main/resources/assets/tfc/models/block/ore/" + grade + "_" + ore[0] + "/" + rock + ".json"
                    dict["parent"] = "tfc:block/ore"
                    dict["textures"] = {}
                    dict["textures"]["all"] = rock_path
                    dict["textures"]["particle"] = rock_path
                    dict["textures"]["overlay"] = overlay_path
                    func.gen_json(dict, file_path)
                    
                    # Ore blockitem models
                    dict = {}
                    parent_path = "tfc:block/ore/" + grade + "_" + ore[0] + "/" + rock
                    file_path = "../src/main/resources/assets/tfc/models/item/ore/" + grade + "_" + ore[0] + "/" + rock + ".json"
                    dict["parent"] = parent_path
                    func.gen_json(dict, file_path)
                    
                # Ore item models
                dict = {}
                texture_path = "tfc:item/ore/" + grade + "_" + ore[0]
                file_path = "../src/main/resources/assets/tfc/models/item/ore/" + grade + "_" + ore[0] + ".json"
                dict["parent"] = "item/generated"
                func.create_nested_dict(["textures", "layer0"], texture_path, dict)
                func.gen_json(dict, file_path)

            # Small ores
            dict = {}
            texture_path = "tfc:item/ore/small_" + ore[0]
            file_path = "../src/main/resources/assets/tfc/models/item/ore/small_" + ore[0] + ".json"
            dict["parent"] = "item/generated"
            func.create_nested_dict(["textures", "layer0"], texture_path, dict)
            func.gen_json(dict, file_path)

        # Non-graded ores
        else:
            for rock in namelist.rocks:
                
                # Ore block models
                dict = {}
                rock_path = "tfc:block/rock/raw/" + rock
                overlay_path = "tfc:block/ore/" + ore[0]
                file_path = "../src/main/resources/assets/tfc/models/block/ore/" + ore[0] + "/" + rock + ".json"
                dict["parent"] = "tfc:block/ore"
                dict["textures"] = {}
                dict["textures"]["all"] = rock_path
                dict["textures"]["particle"] = rock_path
                dict["textures"]["overlay"] = overlay_path
                func.gen_json(dict, file_path)

                # Ore blockitem models
                dict = {}
                parent_path = "tfc:block/ore/" + ore[0] + "/" + rock
                file_path = "../src/main/resources/assets/tfc/models/item/ore/" + ore[0] + "/" + rock + ".json"
                dict["parent"] = parent_path
                func.gen_json(dict, file_path)

                # Ore item models
                dict = {}
                texture_path = "tfc:item/ore/" + ore[0]
                file_path = "../src/main/resources/assets/tfc/models/item/ore/" + ore[0] + ".json"
                dict["parent"] = "item/generated"
                func.create_nested_dict(["textures", "layer0"], texture_path, dict)
                func.gen_json(dict, file_path)


# Generate metal item model files
def metal_model_gen():
    for metal in namelist.metals:
        
        # ingot item models
        dict = {}
        texture_path = "tfc:item/metal/ingot/" + metal[0]
        file_path = "../src/main/resources/assets/tfc/models/item/metal/ingot/" + metal[0] + ".json"
        dict["parent"] = "item/generated"
        func.create_nested_dict(["textures", "layer0"], texture_path, dict)
        func.gen_json(dict, file_path)

        # tool item models
        if metal[1]:
            func.gen_metal_item(namelist.types_tools, metal)

        # basic part item models
        if metal[2]:
            func.gen_metal_item(namelist.types_parts, metal)

        # armor item models
        if metal[3]:
            func.gen_metal_item(namelist.types_armors, metal)
