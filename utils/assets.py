import tfce_utils
import ore_graded
import metal_item

# init lang file
dict = {}
file_path = "../src/main/resources/assets/tfcelem/lang/en_us.json"
tfce_utils.write_json(dict, file_path)

# graded ores
ore_graded.gen_state()
ore_graded.gen_model()
ore_graded.gen_lang()
ore_graded.register_tags()

# metal items
metal_item.gen_model()
metal_item.gen_texture()
metal_item.gen_lang()