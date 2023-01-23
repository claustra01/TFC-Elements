import numpy as np
import cv2

def transpare(bgr_img, bgr_mask, div_range):
    mask = np.all((bgr_img[:,:,:] - bgr_mask) <= div_range, axis=-1)
    bgra_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2BGRA)
    bgra_img[mask, 3] = 0
    return bgra_img


# change HSV
def change_hsv(temp_path, file_path, h, s, v):
    
    temp_img = cv2.imread(temp_path)
    hsv_img = cv2.cvtColor(temp_img, cv2.COLOR_BGR2HSV)
    
    hsv_img[:,:,(0)] = hsv_img[:,:,(0)] + h
    hsv_img[:,:,(1)] = hsv_img[:,:,(1)] + s
    hsv_img[:,:,(2)] = hsv_img[:,:,(2)] + v
    bgr_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
   
    hsv_black = [0, 0, 0]
    hsv_mask = [hsv_black[0]+h, hsv_black[1]+s, hsv_black[2]+v]
    bgr_mask = cv2.cvtColor(np.array([[hsv_mask]], dtype=np.uint8), cv2.COLOR_HSV2BGR)[0][0]
    
    bgra_img = transpare(bgr_img, bgr_mask, 0)
    cv2.imwrite(file_path, bgra_img)


# grayscale
def grayscale(temp_path, file_path):
    gray_img = cv2.imread(temp_path, 0)
    cv2.imwrite(file_path, gray_img)
    bgra_img = transpare(cv2.imread(file_path), [0, 0, 0], 5)
    cv2.imwrite(file_path, bgra_img)
    