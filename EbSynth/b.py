import cv2
import os

# Define the path to the frames and the output video
frames_path = '/Users/lambert/Downloads/EbSynth-Beta-Mac/SampleProject/video'
output_video = '/Users/lambert/Downloads/EbSynth-Beta-Mac/output.mp4'

# Get a list of all frame files in the directory
frame_files = sorted([f for f in os.listdir(frames_path) if f.endswith('.jpg')])

# Read the first frame to get the dimensions
first_frame = cv2.imread(os.path.join(frames_path, frame_files[0]))
height, width, layers = first_frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_video, fourcc, 30.0, (width, height))

# Write each frame to the video
for frame_file in frame_files:
    frame = cv2.imread(os.path.join(frames_path, frame_file))
    video.write(frame)

# Release the video writer
video.release()

# Use ffmpeg to convert the video to a real mp4 format
os.system(f'ffmpeg -i {output_video} -vcodec libx264 {output_video.replace(".mp4", "_converted.mp4")}')