import tfce_utils
import ore_graded
import ore_all
import metal_item
import metal_all

# init lang file
dict = {}
file_path = "../src/main/resources/assets/tfcelem/lang/en_us.json"
tfce_utils.write_json(dict, file_path)

# init ore blocks hardness
dir_path = "../src/main/resources/data/minecraft/tags/blocks"
tfce_utils.create_simple_tag(dir_path, dir_path + "/needs_stone_tool.json", [])
tfce_utils.create_simple_tag(dir_path, dir_path + "/needs_iron_tool.json", [])
tfce_utils.create_simple_tag(dir_path, dir_path + "/needs_diamond_tool.json", [])
dir_path = "../src/main/resources/data/forge/tags/blocks"
tfce_utils.create_simple_tag(dir_path, dir_path + "/needs_netherite_tool.json", [])

# graded ores
ore_graded.gen_state()
ore_graded.gen_model()
ore_graded.gen_lang()
ore_graded.register_tags()

# all ores
ore_all.register_tags()

# metal items
metal_item.gen_model()
metal_item.gen_texture()
metal_item.gen_lang()
metal_item.register_tags()

# all metals
metal_all.register_tags()