import cv2
import numpy as np
from PIL import Image

cap = cv2.VideoCapture('juicy1copy.avi')

while(cap.isOpened()):
	ret, frame = cap.read()
	left_right_image = np.split(frame, 2, axis=1)
	left_img = left_right_image[0]
	right_img = left_right_image[1]
	print (type(left_img))

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()