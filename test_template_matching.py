import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("testCoockie.png")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread("template_coockie.png", 0)

#template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
#methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

#for meth in methods:
img = img2.copy()
#    method = eval(meth)

    # Apply template Matching
res = cv2.matchTemplate(img, template, method=cv2.TM_CCOEFF)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left= max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
print(bottom_right)
cv2.rectangle(img,top_left, bottom_right, 255, 2)

plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#plt.suptitle(meth)

plt.show()

