from moviepy.editor import VideoFileClip, vfx, ColorClip, clips_array, CompositeVideoClip
import os
import shutil
import argparse
from webcolors import name_to_rgb
from tqdm import tqdm

# Define parameters
parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', action="store", type=str, help="The path of the root directory containing *.mp4 files", default='./')
parser.add_argument('--color', action="store", type=str, help="The padding color (list of webcolors)", default="white")

args = parser.parse_args()
padding_color = name_to_rgb(args.color)
input_folder = args.input_folder


def color_clip(size, duration, fps=25, color=(0,0,0), output='color.mp4'):
    return ColorClip(size, color, duration=duration)

if os.path.exists('./tiktok'):
    shutil.rmtree('./tiktok')

os.mkdir('./tiktok')
size = (1080, 1920)
duration = 5

background = color_clip(size, duration, color=padding_color)

file_paths = []

for dirpath, dirnames, filenames in os.walk(input_folder):
    for filename in [f for f in filenames if f.endswith(".mp4")]:
        file_paths.append(os.path.join(dirpath, filename))

print('There are {} videos to convert'.format(len(filenames)))

for idx, file_path in enumerate(file_paths):
    video = VideoFileClip(file_path)
    video = video.resize( (1080,1080) )
    final = CompositeVideoClip([background, video.set_position("center")], size=size)
    final.write_videofile('./tiktok/tt_{}.mp4'.format(idx))
