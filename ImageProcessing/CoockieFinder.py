import cv2
import numpy as np

def find_cookie(img):
    return find_template(img, "img\\Template\\template_coockie.png")

def find_cursor(img):
    return find_template(img, "img\\Template\\template_cursor.png")

def find_grandma(img):
    return find_template(img, "img\\Template\\template_grandma.png")

def find_farm(img):
    return find_template(img, "img\\Template\\template_farm.png")

def find_mine(img):
    return find_template(img, "img\\Template\\template_mine.png")

def find_factory(img):
    return find_template(img, "img\\Template\\template_factory.png")

def find_bank(img):
    return find_template(img, "img\\Template\\template_bank.png")

def find_temple(img):
    return find_template(img, "img\\Template\\template_temple.png")



def find_template(img, template_name):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_name, 0)
    #w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, method=cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_loc
