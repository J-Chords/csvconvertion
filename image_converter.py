import os
import cv2

def images_to_video(image_folder, output_path, frame_rate):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()  # Make sure images are in the correct order

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), frame_rate, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

if __name__ == "__main__":
    image_folder = "images"  # Change this to the path of your image folder
    output_path = "output_video.mp4"  # Change this to the desired output video path
    frame_rate = 24  # Adjust the frame rate as needed

    images_to_video(image_folder, output_path, frame_rate)
    print("Video created successfully!")
