import namelist
import func_image

# Generate metal item image files
def metal_image_gen():
    for metal in namelist.metals:
        
        temp_path = "../src/main/resources/assets/tfc/textures/item/metal/ingot/temp_" + metal[5][0] + ".png"
        file_path = "../src/main/resources/assets/tfc/textures/item/metal/ingot/" + metal[0] + ".png"
        func_image.change_hsv(temp_path, file_path, metal[5][1], metal[5][2], metal[5][3])

        if metal[2]:
            func_image.change_hev_metal_item(namelist.types_parts, metal)

