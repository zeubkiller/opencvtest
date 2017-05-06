import pyautogui
import numpy as np
from ImageProcessing.CoockieFinder import *
import cv2
import collections

def get_current_img():
    pyautogui_img = pyautogui.screenshot()
    open_cv_image = np.array(pyautogui_img) 
    # Convert RGB to BGR 
    return open_cv_image[:, :, ::-1].copy()

def find_cookie_and_move(duration=0):
    pos = find_cookie(get_current_img())
    #print(pos)
    pyautogui.moveTo(pos, duration=duration)

map_building = collections.OrderedDict()




map_building['Temple'] = find_temple
map_building['Bank'] = find_bank
map_building['Factory'] = find_factory
map_building['Mine'] = find_mine
map_building['Farm'] = find_farm
map_building['Grandma'] = find_grandma
map_building['Cursor'] = find_cursor

def find_building_and_move(name, duration=0):
     pos = map_building[name](get_current_img())
     pyautogui.moveTo(pos, duration=duration)

def test_all_building():
    for key in map_building.keys():
        find_building_and_move(key)
        pyautogui.click()


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.001
for i in range(0, 10):
    find_cookie_and_move()
    for i in range(0, 10000):
        pyautogui.click()
    
    for key in map_building.keys():
        find_building_and_move(key)
        pyautogui.click()
