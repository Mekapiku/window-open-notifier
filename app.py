import cv2
import numpy as np

import json
import configparser

# config
config = configparser.ConfigParser()
config.read('./config.ini', 'UTF-8')

## file path
source_path = config.get('file_path', 'source')
output_path = config.get('file_path', 'output')
templace_lock_path = config.get('file_path', 'template_lock')
templace_unlock_path = config.get('file_path', 'template_unlock')

# parameters
threshold = float(config.get('settings', 'threshold'))
mag_size = int(config.get('settings', 'mag_size'))


# source image
screenshot = cv2.imread(source_path)
img_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

# template images
template_lock = cv2.imread(templace_lock_path, 0)
template_unlock = cv2.imread(templace_unlock_path, 0)

# lock matching result
result_lock = cv2.matchTemplate(img_gray, template_lock, cv2.TM_CCOEFF_NORMED)
result_unlock = cv2.matchTemplate(img_gray, template_unlock, cv2.TM_CCOEFF_NORMED)

# filter by threshold
loc_lock = np.where(result_lock >= threshold)
loc_unlock = np.where(result_unlock >= threshold)

# output object
mags = {"mags" : []}

count = 0

# result lock
for pt in zip(*loc_lock[::-1]):
    mags["mags"].append({"id" : count, "state" : "locked"})
    count += 1

# result unlock
for pt in zip(*loc_unlock[::-1]):
    mags["mags"].append({"id" : count, "state" : "unlocked"})
    count += 1

# TODO unkown state
while count < mag_size:
    mags["mags"].append({"id" : count, "state" : "unknown"})
    count += 1

# Output
out = open(output_path, 'w')
json.dump(mags, out, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))