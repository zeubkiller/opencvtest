import cv2

def resize(img):
    """Resize an image to half his size"""
    return cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

def convert_rgb_img(img):
    """Convert a BGR img to RGB"""
    b,g,r = cv2.split(img)
    return cv2.merge((r,g,b))