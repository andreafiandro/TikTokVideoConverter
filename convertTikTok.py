from moviepy.editor import VideoFileClip, vfx, ColorClip, clips_array, CompositeVideoClip
import os
from tqdm import tqdm

def color_clip(size, duration, fps=25, color=(0,0,0), output='color.mp4'):
    return ColorClip(size, color, duration=duration)

if os.path.exists('./tiktok'):
    os.rmdir('./tiktok')
os.mkdir('./tiktok')
size = (1080, 1920)
duration = 5
background = color_clip(size, duration)

file_paths = []

for dirpath, dirnames, filenames in os.walk("./"):
    for filename in [f for f in filenames if f.endswith(".mp4")]:
        file_paths.append(os.path.join(dirpath, filename))

print('Ci sono {} video da convertire in TikTok'.format(len(filenames)))

for idx, file_path in enumerate(file_paths):
    video = VideoFileClip(file_path)
    video = video.resize( (1080,1080) )
    final = CompositeVideoClip([background, video.set_position("center")], size=size)
    final.write_videofile('./tiktok/tt_{}.mp4'.format(idx))
