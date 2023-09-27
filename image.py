from moviepy.editor import ImageSequenceClip
import os

def images_to_video(image_folder, output_path, fps):
    image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(".png")]
    image_files.sort()  # Make sure images are in the correct order

    clip = ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile(output_path, codec='libx264')

if __name__ == "__main__":
    image_folder = 'path_to_your_image_folder'  # Change this to the path of your image folder
    output_path = 'output_video.mp4'  # Change this to the desired output video path
    fps = 24  # Frames per second for the output video

    images_to_video(image_folder, output_path, fps)
    print("Video created successfully!")
