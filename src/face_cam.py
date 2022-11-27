import cv2
import os

path = os.path.abspath('face_dataset')
if not os.path.isdir(path):
    print("No such a directory: {}".format(path))
vid = cv2.VideoCapture(0)
k=1
while(True):
  ret, frame = vid.read()
  cv2.imshow('frame', frame)
  if cv2.waitKey(1) == ord('s'):
    cv2.imshow('face_'+str(k), frame)
    # cv2.imwrite('/Home/Desktop/Spectres-Inheritance/face_'+str(k)+'.png', frame)
    cv2.imwrite(os.path.join(path, 'face_'+str(k)+'.png'), frame)
    k=k+1
  elif cv2.waitKey(1)== ord('q'):
    break
vid.release()
cv2.destroyAllWindows()
