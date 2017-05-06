import cv2

def resize(img):
    """Resize an image to half his size"""
    return cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
