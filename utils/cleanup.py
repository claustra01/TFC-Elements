import os
import glob
import cv2
import tfce_types
import tfce_images

def cleanup_metal_parts(dir_path):
    files = glob.glob(dir_path + "/*")
    for file_path in files:
        if "\wrought_iron.png" in file_path:
            tfce_images.grayscale(file_path, dir_path + "/iron_base.png")
        elif "\silver.png" in file_path:
            tfce_images.grayscale(file_path, dir_path + "/silver_base.png")
        elif "\steel.png" in file_path:
            result_path = dir_path + "/steel_base.png"
            tfce_images.grayscale(file_path, result_path)
            tfce_images.change_hsv(result_path, result_path, 0, 0, 30)
        if not "base.png" in file_path:
            os.remove(file_path)


def cleanup_metal_tools(dir_path):
    files = glob.glob(dir_path + "/*")
    for file_path in files:
        if "\wrought_iron.png" in file_path:
            tfce_images.grayscale(file_path, dir_path + "/base.png")
        if not ("base.png" in file_path or "\wrought_iron.png" in file_path):
            os.remove(file_path)


cleanup_metal_parts("../src/main/resources/assets/tfc/textures/item/metal/ingot")
for type in tfce_types.types_parts:
    cleanup_metal_parts("../src/main/resources/assets/tfc/textures/item/metal/" + type)
for type in tfce_types.types_tools:
    cleanup_metal_tools("../src/main/resources/assets/tfc/textures/item/metal/" + type)
