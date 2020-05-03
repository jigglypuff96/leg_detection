import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened() == False): 
	print("Unable to read camera feed")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.

# outleft = cv2.VideoWriter('outleft.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
# outright = cv2.VideoWriter('outright.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

save_folder = './images/test/'
attr = 'juicy1'
out = cv2.VideoWriter(attr+'outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

i= 0
while(True):
	ret, frame = cap.read()

	if ret == True: 
		# outleft.write(frame[0:round(frame_width/2),0:frame_height])
		# outright.write(frame[round(frame_width/2):frame_width,0:frame_height])
		# Write the frame into the file 'output.avi'
		out.write(frame)

		# Display the resulting frame    
		cv2.imshow('frame',frame)

		left_right_image = np.split(frame, 2, axis=1)        # Display images
		left_img = left_right_image[0]
		right_img = left_right_image[1]
		cv2.imwrite(save_folder+attr+'left'+str(i)+'.png', left_img)
		cv2.imwrite(save_folder+attr+'right'+str(i)+'.png', right_img)
		i += 1

		# Press Q on keyboard to stop recording
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# Break the loop
	else:
		break  

# When everything done, release the video capture and video write objects
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows() 
