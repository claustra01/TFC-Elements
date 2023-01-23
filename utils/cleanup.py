import os
import glob
import tfce_types
import tfce_images

def cleanup_metal_items(dir_path):
    files = glob.glob(dir_path + "/*")
    for file_path in files:
        if "\wrought_iron.png" in file_path:
            tfce_images.grayscale(file_path, dir_path + "/iron_type.png")
        elif "\silver.png" in file_path:
            tfce_images.grayscale(file_path, dir_path + "/silver_type.png")
        elif "\steel.png" in file_path:
            result_path = dir_path + "/steel_type.png"
            tfce_images.grayscale(file_path, result_path)
            tfce_images.change_hsv(result_path, result_path, 0, 0, 30)
        if not "type.png" in file_path:
            os.remove(file_path)

def cleanup_metal_tools(dir_path):
    return

dir_path = "../src/main/resources/assets/tfc/textures/item/metal/" + "ingot"
cleanup_metal_items(dir_path)