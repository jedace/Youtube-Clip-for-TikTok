from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip

# Get the URL of the YouTube video from the user
video_url = input("Enter the URL of the YouTube video: ")

# Download the video from YouTube
yt = YouTube(video_url)
video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

# Cut the video into x-second long clips, where i = clip length
video_clip = VideoFileClip(video)
duration = video_clip.duration

for i in range(0, int(duration), 98):
    start_time = i
    end_time = min(i + 98, duration)
    clip = video_clip.subclip(start_time, end_time)
    clip.write_videofile(f"clip_{i}.mp4")
