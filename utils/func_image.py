import numpy as np
import cv2

# Change HSV
def change_hsv(temp_path, file_path, h, s, v):
    
    temp_img = cv2.imread(temp_path)
    hsv_img = cv2.cvtColor(temp_img, cv2.COLOR_BGR2HSV)
    
    hsv_img[:,:,(0)] = hsv_img[:,:,(0)] + h
    hsv_img[:,:,(1)] = hsv_img[:,:,(1)] + s
    hsv_img[:,:,(2)] = hsv_img[:,:,(2)] + v
    
    hsv_white = [0, 0, 255]
    hsv_mask = [hsv_white[0]+h, hsv_white[1]+s, hsv_white[2]+v]
    bgr_mask = cv2.cvtColor(np.array([[hsv_mask]], dtype=np.uint8), cv2.COLOR_HSV2BGR)[0][0]
    
    bgr_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
    mask = np.all(bgr_img[:,:,:] == bgr_mask, axis=-1)
    bgra_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2BGRA)
    bgra_img[mask, 3] = 0
    
    cv2.imwrite(file_path, bgra_img)


# Change HSV metal item image
def change_hev_metal_item(types, metal):
    for type in types:
        temp_path = "../src/main/resources/assets/tfc/textures/item/metal/" + type + "/temp_" + metal[5][0] + ".png"
        file_path = "../src/main/resources/assets/tfc/textures/item/metal/" + type + "/" + metal[0] + ".png"
        change_hsv(temp_path, file_path, metal[5][1], metal[5][2], metal[5][3])
