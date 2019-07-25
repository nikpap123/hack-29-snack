import cv2
import glob
import pandas as pd
from collections import defaultdict


existsQ = []
def detect_rl_click(event,x,y,flags,param):
    global existsQ
    if event == 1:
        cv2.circle(imageS,(x,y),10,(230,0,0),-1)
        existsQ.append(1)
        print('left')
    elif event == 2:
        print('right')
        cv2.circle(imageS,(x,y),10,(0, 0,230),-1)
        existsQ.append(0)

lables = defaultdict(list)
for imfile in glob.glob('data/*.jpg'):
    image = cv2.imread(imfile)
    imageS = cv2.resize(image, (960, 960))
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',detect_rl_click)
    while(1):
        cv2.imshow('image',imageS)
        k = cv2.waitKey(20) & 0xFF
        if k == ord('x'):
            lables['filename'].append(imfile)
            existsQstr = [str(x) for x in existsQ]
            lables['labels'].append(','.join(existsQstr))
            existsQ = []
            break
        elif k == ord('a'):
            print('sanity checking lables')
            print('{} snacks labled'.format(len(existsQ)))
            print('{} available snacks'.format(sum(existsQ)))
            print('{} unavailable snacks'.format(len(existsQ) - sum(existsQ)))
            print(existsQ)

pd.DataFrame(lables).to_csv('train_lables.csv')
