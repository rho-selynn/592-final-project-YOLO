import os
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
import time

times = []
for i in range(20):
    time_start = time.time()
    os.system('libcamera-still -o ../Various_Data/Captured_Images/test1.jpg -t 1 -n --width 1360 --height 800 --exposure sport')
    os.system('python3 /home/mdholm/Desktop/592_Stuff/Various_Data/yolov5-master/yolov5-master/detect.py --weights /home/mdholm/Desktop/592_Stuff/Saved_Neural_Networks/Original_YOLO.pt --img 1360 --conf 0.3 --source ../Various_Data/Captured_Images/test1.jpg')
    plt.clf()
    image = img.imread('/home/mdholm/Desktop/592_Stuff/Various_Data/yolov5-master/yolov5-master/runs/detect/exp/test1.jpg')
    plt.imshow(image)
    plt.draw
    plt.pause(.001)
    os.system('rm /home/mdholm/Desktop/592_Stuff/Various_Data/yolov5-master/yolov5-master/runs/detect/exp/test1.jpg')
    os.system('rm /home/mdholm/Desktop/592_Stuff/Various_Data/yolov5-master/yolov5-master/runs/detect/exp -d')
    time_end = time.time() - time_start
    times.append(time_end)
    plt.close()
del times[0]
plt.plot(times)
plt.show()
print(sum(times)/len(times))
