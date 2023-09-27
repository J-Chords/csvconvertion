import cv2
import os

path = 'images/'  # Make sure to include a trailing slash
out_path = ''
out_video_name = 'fading_cube2.mp4'
out_video_full_path = os.path.join(out_path, out_video_name)  # Use os.path.join to construct paths

pre_imgs = os.listdir(path)
img = []

for i in pre_imgs:
    img_path = os.path.join(path, i)  # Construct the full path to the image
    img.append(img_path)

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

frame = cv2.imread(img[0])

if frame is not None:  # Check if the image is read successfully
    size = frame.shape[:2][::-1]  # Get the size from the image shape
    video = cv2.VideoWriter(out_video_full_path, cv2_fourcc, 24, size)

    for i in range(len(img)):
        frame = cv2.imread(img[i])
        if frame is not None:
            video.write(frame)
            print('frame', i+1, 'of', len(img))
        else:
            print('Could not read frame', i+1)

    video.release()
    print('Outputted video to', out_video_full_path)
else:
    print('Could not read the first image:', img[0])
