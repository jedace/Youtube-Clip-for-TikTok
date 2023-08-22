from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
from datetime import datetime

# Get the URL of the YouTube video from the user
video_url = input("Enter the URL of the YouTube video: ")

# Download the highest resolution stream from YouTube
yt = YouTube(video_url)
video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

# Cut the video into 61-second long clips
video_clip = VideoFileClip(video)
duration = video_clip.duration

# Get the current timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

for i in range(0, int(duration), 61):
    start_time = i
    end_time = min(i + 61, duration)
    clip = video_clip.subclip(start_time, end_time)
    clip.write_videofile(f"clip_{timestamp}_{i}.mp4")
