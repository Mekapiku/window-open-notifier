import sys
import cv2
import numpy as np

import json

if len(sys.argv) < 4:
    sys.exit(-1)

## file path
output_path = sys.argv[1]
source_path = sys.argv[2]
templace_lock_path = "template/lock.png"
templace_unlock_path = "template/unlock.png"

# parameters
threshold = 0.99
mag_size = int(sys.argv[3])

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

# reformat result to hash
leafee_list = []

# locked objects
loc_x = loc_lock[0]; loc_y = loc_lock[1]
index = 0
while index < len(loc_x):
    leafee_list.append({"x":loc_x[index], "y":loc_y[index], "state":"locked"})
    index += 1

# unlocked objects
loc_x = loc_unlock[0]; loc_y = loc_unlock[1]
index = 0
while index < len(loc_x):
    leafee_list.append({"x":loc_x[index], "y":loc_y[index], "state":"unlocked"})
    index += 1

# Sort By x -> y
# example: id1 -> 0, 0, id2 -> 100, 0
#          id3 -> 0, 100, ...
sorted_leafee_list = sorted(
  leafee_list,
  key = lambda x: (x["y"], x["x"])
)

# output leafee
leafee = {}; leafee["leafee"] = []

# reformat result hash to json
count = 0
for item in sorted_leafee_list:
    leafee["leafee"].append({"id" : count, "state" : item["state"]})
    count += 1

# TODO unkown state
while count < mag_size:
    leafee["leafee"].append({"id" : count, "state" : "unknown"})
    count += 1

# Output
with open(output_path, 'w') as out:
    json.dump(leafee, out, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
