import namelist
import func

# Generate ore blockstate files
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
            texture_path = "tfc:item/ore/small_" + ore[0]
            file_path = "../src/main/resources/assets/tfc/models/item/ore/" + grade + "_" + ore[0] + ".json"
            dict["parent"] = "item/generated"
            func.create_nested_dict(["textures", "layer0"], texture_path, dict)
            func.gen_json(dict, file_path)

        # Small ores
        dict = {}

    # Non-graded ores
    else:
        for rock in namelist.rocks:
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
