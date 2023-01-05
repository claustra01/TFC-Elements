import namelist
import func

# Ore Translation
def gen_ore_lang():
    
    # Read lang file
    dict = {}
    
    for ore in namelist.ores:
        
        # Graded ores
        if ore[1]:
            for grade in namelist.grades:
                for rock in namelist.rocks:
        
                    trans_key = "block.tfc.ore." + grade + "_" + ore[0] + "." + rock
                    display_name = grade.title() + " " + rock.title() + " " + ore[0].replace("_", " ").title() + " Ore"
                    dict[trans_key] = display_name
    

    # Write lang file
    file_path = "../src/main/resources/assets/tfc/lang/en_us.json"
    func.gen_json(dict, file_path)