import cv2 as cv
import pyscreenshot as pys
import numpy as np

fourcc = cv.VideoWriter_fourcc('M','P','E','G')
out = cv.VideoWriter('output.avi', fourcc, 8, (1920,1080))
list_of_frame = []
i = 0
flag = True
while flag:
    img = pys.grab()
    img = np.array(img)
  
    list_of_frame.append(img)

    if i==100:
        break
    i+=1
    # if cv.waitKey(20) & 0xFF==ord('q'):
    #     break

for frame in list_of_frame:
    out.write(frame)
out.release()