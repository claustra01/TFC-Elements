import namelist
import func

# Generate ore blockstate files
def ore_blockstate_gen():
    for ore in namelist.ores:
        
        # Graded ores
        if ore[1]:
            for grade in namelist.grades:
                for rock in namelist.rocks:
                    
                    # Ore blocks
                    dict = {}
                    model_path = "tfc:block/ore/" + grade + "_" + ore[0] + "/" + rock
                    file_path = "../src/main/resources/assets/tfc/blockstates/ore/" + grade + "_" + ore[0] + "/" + rock + ".json"
                    func.gen_nested_dict(["variants", "", "model"], model_path, dict)
                    func.gen_json(dict, file_path)
                    
            # Small ores
            dict = {}
            model_path = "tfc:block/groundcover/" + ore[0]
            file_path = "../src/main/resources/assets/tfc/blockstates/ore/small_" + ore[0] + ".json"
            func.gen_nested_dict(["variants", ""], [{}, {}, {}, {}], dict)
            dict["variants"][""][0] = {"model": model_path, "y": 90}
            dict["variants"][""][1] = {"model": model_path}
            dict["variants"][""][2] = {"model": model_path, "y": 180}
            dict["variants"][""][3] = {"model": model_path, "y": 270}
            func.gen_json(dict, file_path)

        # Non-graded ores
        else:
            for rock in namelist.rocks:
                dict = {}
                model_path = "tfc:block/ore/" + ore[0] + "/" + rock
                file_path = "../src/main/resources/assets/tfc/blockstates/ore/" + ore[0] + "/" + rock + ".json"
                func.gen_nested_dict(["variants", "", "model"], model_path, dict)
                func.gen_json(dict, file_path)
