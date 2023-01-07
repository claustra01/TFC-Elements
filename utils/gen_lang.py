import namelist
import func

def gen_lang():
    dict = {}

    # Ore Translation
    for ore in namelist.ores:
        
        # Graded ores
        if ore[1]:
            for grade in namelist.grades:
                for rock in namelist.rocks:
        
                    trans_key = "block.tfc.ore." + grade + "_" + ore[0] + "." + rock
                    display_name = grade.title() + " " + rock.title() + " " + ore[0].replace("_", " ").title() + " Ore"
                    dict[trans_key] = display_name

                trans_key = "item.tfc.ore." + grade + "_" + ore[0]
                display_name = grade.title() + " " + ore[0].replace("_", " ").title() + " Ore"
                dict[trans_key] = display_name
            
            trans_key = "block.tfc.ore.small_"  + ore[0]
            display_name = "Small " + ore[0].replace("_", " ").title() + " Ore"
            dict[trans_key] = display_name

    # Metal Item Translation
    for metal in namelist.metals:
        
        trans_key = "metal.tfc." + metal[0]
        display_name = metal[0].replace("_", " ").title()
        dict[trans_key] = display_name

        trans_key = "item.tfc.metal.ingot." + metal[0]
        display_name = metal[0].replace("_", " ").title() + " Ingot"
        dict[trans_key] = display_name

        if metal[1]:
            dict = func.trans_metal_item(namelist.types_tools, metal, dict)

        if metal[2]:
            dict = func.trans_metal_item(namelist.types_parts, metal, dict)

        if metal[3]:
            dict = func.trans_metal_item(namelist.types_armors, metal, dict)
    

    # Write lang file
    file_path = "../src/main/resources/assets/tfcelem/lang/en_us.json"
    func.gen_json(dict, file_path)