import cv2
import os

input_folder = 'frame'
output_folder = 'resized_frames'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img = cv2.imread(os.path.join(input_folder, filename))
        resized_img = cv2.resize(img, (1280, 720))
        cv2.imwrite(os.path.join(output_folder, filename), resized_img)

        